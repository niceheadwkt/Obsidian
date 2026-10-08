#!/usr/bin/env bash
# 清除跨電腦經雲端硬碟同步造成的 git 假修改：
# git status 顯示 M、但忽略換行差異後內容完全相同的檔案，以 git add 刷新 index（不產生 commit）。
cd "${CLAUDE_PROJECT_DIR:-.}" 2>/dev/null || exit 0
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || exit 0

cleaned=()
while IFS= read -r -d '' entry; do
  # 只處理「工作區已修改、暫存區未動」的檔案（狀態碼 " M"）
  [ "${entry:0:2}" = " M" ] || continue
  f=${entry:3}
  if git diff --quiet --ignore-cr-at-eol -- "$f" 2>/dev/null; then
    git add -- "$f" 2>/dev/null || continue
    # 若加入後與 HEAD 仍有差異（如 autocrlf=false 時的換行變更），撤回，避免誤入下次 commit
    if git diff --cached --quiet -- "$f" 2>/dev/null; then
      cleaned+=("$f")
    else
      git reset -q -- "$f" 2>/dev/null
    fi
  fi
done < <(git -c core.quotepath=false status --porcelain=v1 -z --untracked-files=no 2>/dev/null)

if [ ${#cleaned[@]} -gt 0 ]; then
  list=$(printf '%s、' "${cleaned[@]}")
  list=${list%、}
  msg="已自動清除 ${#cleaned[@]} 個跨電腦同步造成的 git 假修改（內容未變）：${list}"
  PYTHONIOENCODING=utf-8 python -c 'import json,sys; print(json.dumps({"systemMessage": sys.argv[1]}, ensure_ascii=False))' "$msg" 2>/dev/null
fi
exit 0
