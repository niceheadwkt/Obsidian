#!/usr/bin/env python3
"""LLM Wiki 維護工具（供 wiki-ingest／wiki-lint 兩個 skill 使用）。

用法：
  python AI/scripts/wiki_tool.py pending [--limit N]   列出尚未匯入 Wiki 的 raw 素材
  python AI/scripts/wiki_tool.py check 頁面 [頁面...]   入庫評分檢查（頁面可用名稱或路徑）
  python AI/scripts/wiki_tool.py lint [--stale-days N]  全庫健康檢查報告
  python AI/scripts/wiki_tool.py hubs [--top N]         被連最多的頁面

check 有任何 FAIL 時結束碼為 1；其餘指令正常結束碼為 0。
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

VAULT = Path(__file__).resolve().parents[2]
AI_DIR = VAULT / "AI"
WIKI = AI_DIR / "wiki"
RAW = AI_DIR / "raw"
SKIP_DIRS = {".git", ".obsidian", ".trash", "node_modules", ".claude"}
SPECIAL = {"index", "log", "README"}


def in_index(name, index_text):
    r"""判斷頁面是否列在 index.md。
    支援 [[頁名]]、[[頁名|別名]]，以及表格內為了跳脫直線而寫的 [[頁名\|別名]]。"""
    return any(f"[[{name}{tail}" in index_text for tail in ("]]", "|", "\\|"))


PAGE_TYPES = {"concept", "entity", "source-summary", "analysis"}
REQUIRED_FIELDS = ["type", "tags", "sources", "created", "updated"]
# 自此日期起建立的頁面，才要求「一句話重點」與「我可以怎麼用」（舊頁不追溯）
NEW_RULE_DATE = "2026-11-18"
ONE_LINER_MAX = 30

LINK_RE = re.compile(r"\[\[([^\]\|#]*)(?:#[^\]\|]*)?(?:\|[^\]]*)?\]\]")
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
ONE_LINER_RE = re.compile(r"^\*\*一句話重點\*\*[：:]\s*(.+?)\s*$", re.M)
USE_HEADING_RE = re.compile(r"^#{2,3}\s*(?:[一二三四五六七八九十]+、)?\s*我可以怎麼用", re.M)


# ---------- 基礎 ----------

def extract_links(text: str) -> list[str]:
    """取出 [[連結]] 目標；略過程式碼區塊與行內程式碼，並處理表格內的 \\| 跳脫。

    注意：index.md 的連結都包在行內程式碼裡，因此 index 只用純文字比對，不走這裡。
    """
    return [m.group(1).strip().rstrip("\\").strip() for m in LINK_RE.finditer(CODE_RE.sub("", text))]

def build_file_index():
    """vault 內所有檔案：(相對路徑集合, 檔名→路徑對照)。"""
    rel_paths, by_name = set(), defaultdict(list)
    for p in VAULT.rglob("*"):
        if any(part in SKIP_DIRS for part in p.relative_to(VAULT).parts):
            continue
        if p.is_file():
            rel = p.relative_to(VAULT).as_posix()
            rel_paths.add(rel.lower())
            by_name[p.name.lower()].append(rel)
            if p.suffix.lower() == ".md":
                by_name[p.stem.lower()].append(rel)
    return rel_paths, by_name


def resolve(target: str, files) -> bool:
    rel_paths, by_name = files
    t = target.strip().replace("\\", "/")
    if not t:
        return True  # [[#章節]] 指向本頁
    if "/" in t:
        for base in ("", "AI/", "AI/wiki/"):
            for cand in (base + t, base + t + ".md"):
                if cand.lower() in rel_paths:
                    return True
        return False
    return t.lower() in by_name or (t + ".md").lower() in by_name


def split_frontmatter(text: str):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end < 0:
        return None, text
    return text[3:end], text[end + 4:]


def fm_fields(fm: str) -> dict:
    out = {}
    for m in re.finditer(r"^(\w+):\s*(.*)$", fm, re.M):
        out[m.group(1)] = m.group(2).strip()
    return out


def load_pages():
    pages = {}
    for p in sorted(WIKI.glob("*.md")):
        text = p.read_text(encoding="utf-8", errors="replace")
        fm, body = split_frontmatter(text)
        pages[p.stem] = {
            "path": p,
            "text": text,
            "fm": fm,
            "fields": fm_fields(fm) if fm is not None else {},
            "body": body,
            "links": extract_links(text),
            "fm_links": extract_links(fm or ""),
        }
    return pages


def wiki_target(link: str, pages) -> str | None:
    """若連結指向某個 wiki 頁面，回傳該頁名稱。"""
    name = link.replace("\\", "/").rsplit("/", 1)[-1]
    if name.lower().endswith(".md"):
        name = name[:-3]
    if "/" in link and not link.replace("\\", "/").lstrip("/").lower().startswith(("ai/wiki/", "wiki/")):
        return None
    return name if name in pages else None


def inbound_map(pages):
    inbound = defaultdict(set)
    for src, info in pages.items():
        if src in SPECIAL:
            continue
        for link in info["links"]:
            tgt = wiki_target(link, pages)
            if tgt and tgt != src:
                inbound[tgt].add(src)
    return inbound


def find_page(arg: str, pages) -> str | None:
    p = Path(arg)
    stem = p.stem if p.suffix.lower() == ".md" else p.name
    return stem if stem in pages else None


# ---------- pending ----------

def cmd_pending(args):
    pages = load_pages()
    corpus = "\n".join(info["text"] for info in pages.values())
    raws = sorted(p for p in RAW.rglob("*.md"))
    todo = [p for p in raws if p.stem not in corpus]
    print(f"raw 素材共 {len(raws)} 篇，尚未被 Wiki（含 log）引用：{len(todo)} 篇")
    for p in todo[: args.limit] if args.limit else todo:
        print(f"- {p.relative_to(VAULT).as_posix()}")


# ---------- check ----------

def cmd_check(args):
    pages = load_pages()
    files = build_file_index()
    inbound = inbound_map(pages)
    index_text = pages.get("index", {}).get("text", "")
    log_text = pages.get("log", {}).get("text", "")
    any_fail = False

    for arg in args.pages:
        name = find_page(arg, pages)
        print(f"\n## {arg}")
        if not name:
            print("FAIL 找不到此 Wiki 頁面（請放在 AI/wiki/ 底下）")
            any_fail = True
            continue
        info = pages[name]
        f = info["fields"]
        results = []

        def add(ok, msg, level="FAIL"):
            results.append(("PASS" if ok else level, msg))

        add(info["fm"] is not None, "有 YAML frontmatter")
        missing = [k for k in REQUIRED_FIELDS if k not in f]
        add(not missing, "frontmatter 欄位齊全" + (f"（缺：{'、'.join(missing)}）" if missing else ""))
        add(f.get("type") in PAGE_TYPES, f"type 合法（目前：{f.get('type', '無')}）")
        for k in ("created", "updated"):
            add(bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", f.get(k, ""))), f"{k} 日期格式 YYYY-MM-DD")
        today = dt.date.today().isoformat()
        add(f.get("updated") == today, f"updated 為今天（{today}）", level="WARN")

        src_links = info["fm_links"]
        add(len(src_links) > 0, f"sources 至少一個來源連結（目前 {len(src_links)} 個）")
        bad_src = [l for l in src_links if not resolve(l, files)]
        add(not bad_src, "sources 連結都存在" + (f"（失效：{bad_src}）" if bad_src else ""))

        out_wiki = {wiki_target(l, pages) for l in info["links"]} - {None, name} - SPECIAL
        add(len(out_wiki) >= 1, f"連到至少一篇其他 Wiki 頁（目前 {len(out_wiki)} 篇）")
        broken = sorted({l for l in info["links"] if not resolve(l, files)})
        add(not broken, "內文無斷鏈" + (f"（斷鏈：{broken}）" if broken else ""))
        add(len(inbound[name]) >= 1, f"有其他 Wiki 頁回連（雙向連結，目前 {len(inbound[name])} 篇）")

        add(in_index(name, index_text), "已列入 index.md")
        add(name in log_text, "log.md 有記錄此頁")

        if f.get("created", "") >= NEW_RULE_DATE:
            if f.get("type") in ("source-summary", "analysis"):
                m = ONE_LINER_RE.search(info["body"])
                if not m:
                    add(False, "有「**一句話重點**：」行")
                else:
                    n = len(re.sub(r"\s|\*", "", m.group(1)))
                    add(n <= ONE_LINER_MAX, f"一句話重點不超過 {ONE_LINER_MAX} 字（目前 {n} 字）")
            add(bool(USE_HEADING_RE.search(info["body"])), "有「我可以怎麼用」段落")

        fails = sum(1 for s, _ in results if s == "FAIL")
        any_fail |= fails > 0
        for s, msg in results:
            print(f"{s} {msg}")
        passed = sum(1 for s, _ in results if s == "PASS")
        print(f"→ 得分 {passed}/{len(results)}，FAIL {fails} 項")

    sys.exit(1 if any_fail else 0)


# ---------- lint ----------

def cmd_lint(args):
    pages = load_pages()
    files = build_file_index()
    inbound = inbound_map(pages)
    index_text = pages.get("index", {}).get("text", "")
    normal = {k: v for k, v in pages.items() if k not in SPECIAL}
    today = dt.date.today()

    print(f"# Wiki 健康檢查報告（{today.isoformat()}）\n")
    print(f"- Wiki 頁面：{len(normal)} 頁（不含 index／log／README）")
    types = Counter(v["fields"].get("type", "（無）") for v in normal.values())
    print("- 類型分佈：" + "、".join(f"{k} {n}" for k, n in types.most_common()))

    # 斷鏈
    broken_by_page, broken_targets = {}, Counter()
    for name, info in pages.items():
        if name == "log":
            continue  # 日誌為歷史紀錄，不檢查
        b = sorted({l for l in info["links"] if not resolve(l, files)})
        if b:
            broken_by_page[name] = b
            broken_targets.update(b)
    print(f"\n## 1. 斷鏈（{sum(len(v) for v in broken_by_page.values())} 個，分佈於 {len(broken_by_page)} 頁）")
    for name, b in broken_by_page.items():
        print(f"- [[{name}]]：" + "、".join(f"`{x}`" for x in b))

    print("\n## 2. 被多次提到卻沒有頁面的目標（候選新概念頁）")
    cands = [(t, n) for t, n in broken_targets.most_common() if n >= 2]
    print("\n".join(f"- `{t}`（{n} 處）" for t, n in cands) or "- 無")

    print("\n## 2b. 包在反引號裡的連結（Obsidian 不當成連結、關係圖沒有線；示範語法可忽略）")
    code_links = {}
    for name, info in normal.items():
        inner = [l for span in CODE_RE.findall(info["body"]) for l in extract_links(span.strip("`"))]
        if inner:
            code_links[name] = inner
    for name, ls in sorted(code_links.items(), key=lambda kv: -len(kv[1])):
        uniq = list(dict.fromkeys(ls))
        print(f"- [[{name}]]：{len(ls)} 處（" + "、".join(uniq[:6]) + ("…" if len(uniq) > 6 else "") + "）")
    if not code_links:
        print("- 無")

    print("\n## 3. 孤立頁面（沒有其他 Wiki 頁回連；index 不算）")
    orphans = [n for n in normal if not inbound[n]]
    print("\n".join(f"- [[{n}]]" for n in orphans) or "- 無")

    print("\n## 4. 未列入 index.md 的頁面")
    not_idx = [n for n in normal if not in_index(n, index_text)]
    print("\n".join(f"- [[{n}]]" for n in not_idx) or "- 無")

    print("\n## 5. frontmatter 問題")
    fm_issues = []
    for n, info in normal.items():
        f = info["fields"]
        if info["fm"] is None:
            fm_issues.append(f"- [[{n}]]：沒有 frontmatter")
            continue
        miss = [k for k in REQUIRED_FIELDS if k not in f]
        if miss:
            fm_issues.append(f"- [[{n}]]：缺 {'、'.join(miss)}")
        if f.get("type") and f["type"] not in PAGE_TYPES:
            fm_issues.append(f"- [[{n}]]：type 不合法（{f['type']}）")
        bad = [l for l in info["fm_links"] if not resolve(l, files)]
        if bad:
            fm_issues.append(f"- [[{n}]]：sources 失效 {bad}")
    print("\n".join(fm_issues) or "- 無")

    print(f"\n## 6. 超過 {args.stale_days} 天未更新的頁面（可能過時）")
    stale = []
    for n, info in normal.items():
        try:
            d = dt.date.fromisoformat(info["fields"].get("updated", ""))
        except ValueError:
            continue
        if (today - d).days > args.stale_days:
            stale.append((d, n))
    print("\n".join(f"- [[{n}]]（{d}）" for d, n in sorted(stale)) or "- 無")

    print("\n## 7. 現有衝突標記（[!WARNING] 內含「衝突／矛盾」者；一般提醒不列）")
    warn_re = re.compile(r"^> \[!WARNING\][^\n]*\n(?:>[^\n]*\n?)*", re.M)
    warns = []
    for n, info in normal.items():
        hits = [b for b in warn_re.findall(info["text"]) if re.search("衝突|矛盾", b)]
        if hits:
            warns.append(f"- [[{n}]]：{len(hits)} 處")
    print("\n".join(warns) or "- 無")

    print("\n## 8. raw 素材狀況")
    corpus = "\n".join(info["text"] for info in pages.values())
    raws = list(RAW.rglob("*.md"))
    todo = [p for p in raws if p.stem not in corpus]
    others = [p for p in RAW.iterdir() if p.is_file() and p.suffix.lower() != ".md"]
    print(f"- 尚未匯入：{len(todo)}／{len(raws)} 篇（`wiki_tool.py pending` 看清單）")
    print(f"- raw 根目錄非 Markdown 檔：{len(others)} 個（建議集中到附件資料夾）")

    print("\n## 9. 樞紐頁面（被連最多，前 10）")
    for n, s in sorted(inbound.items(), key=lambda kv: -len(kv[1]))[:10]:
        print(f"- [[{n}]]：{len(s)} 篇回連")


def cmd_hubs(args):
    pages = load_pages()
    inbound = inbound_map(pages)
    for n, s in sorted(inbound.items(), key=lambda kv: -len(kv[1]))[: args.top]:
        print(f"{len(s):3d}  {n}")


def main():
    ap = argparse.ArgumentParser(description="LLM Wiki 維護工具")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("pending"); p.add_argument("--limit", type=int, default=0); p.set_defaults(fn=cmd_pending)
    p = sub.add_parser("check"); p.add_argument("pages", nargs="+"); p.set_defaults(fn=cmd_check)
    p = sub.add_parser("lint"); p.add_argument("--stale-days", type=int, default=120); p.set_defaults(fn=cmd_lint)
    p = sub.add_parser("hubs"); p.add_argument("--top", type=int, default=15); p.set_defaults(fn=cmd_hubs)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
