# -*- coding: utf-8 -*-
"""
影片配音標準工具：依 JSON 旁白稿產生 TTS 語音，並合成到影片（取代原音軌）。

用法：
    python voiceover.py 旁白稿.json            # 產生語音 + 合成影片
    python voiceover.py 旁白稿.json --tts-only # 只產生語音、檢查時間是否重疊
    python voiceover.py 旁白稿.json --only 3   # 只重產第 3 段語音（1 起算）後再合成

輸出：與原影片同資料夾，檔名加 `_配音.mp4`（原檔不動）。
"""
import argparse
import asyncio
import json
import re
import subprocess
import sys
from pathlib import Path

import truststore

truststore.inject_into_ssl()  # 公司網路 SSL 檢查，edge-tts 需要

import edge_tts  # noqa: E402

FFMPEG = r"C:\Users\ch26669\AppData\Local\anaconda3\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
DEFAULT_VOICE = "zh-TW-YunJheNeural"  # 台灣腔男聲
DEFAULT_RATE = "+5%"


def media_duration(path):
    """用 ffmpeg -i 讀取媒體長度（秒）。"""
    r = subprocess.run([FFMPEG, "-nostdin", "-i", str(path)],
                       capture_output=True, encoding="utf-8", errors="replace")
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    if not m:
        sys.exit(f"讀不到長度：{path}")
    h, mi, s = m.groups()
    return int(h) * 3600 + int(mi) * 60 + float(s)


async def tts(text, voice, rate, out, retries=8):
    for i in range(retries):
        try:
            await edge_tts.Communicate(text, voice, rate=rate).save(str(out))
            return
        except Exception as e:  # 微軟服務偶發 No audio / WinError 64，重試即可
            print(f"  TTS 失敗（第 {i + 1} 次）：{str(e)[:80]}")
            await asyncio.sleep(2)
    sys.exit(f"TTS 連續失敗，請確認網路後重跑：{text}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script", help="旁白稿 JSON")
    ap.add_argument("--tts-only", action="store_true", help="只產生語音不合成")
    ap.add_argument("--only", type=int, nargs="*", help="只重產指定段落（1 起算）")
    args = ap.parse_args()

    cfg_path = Path(args.script).resolve()
    cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
    video = (cfg_path.parent / cfg["video"]).resolve()
    voice = cfg.get("voice", DEFAULT_VOICE)
    rate = cfg.get("rate", DEFAULT_RATE)
    segs = sorted(cfg["segments"], key=lambda s: s["t"])
    work = cfg_path.parent / (cfg_path.stem + "_tts")
    work.mkdir(exist_ok=True)

    # 1. 產生各段語音
    for i, s in enumerate(segs, 1):
        mp3 = work / f"{i:02d}.mp3"
        if args.only and i not in args.only and mp3.exists():
            continue
        print(f"[{i:02d}] {s['t']:>6.1f}s  {s['text']}")
        asyncio.run(tts(s["text"], s.get("voice", voice), s.get("rate", rate), mp3))

    # 2. 檢查時間重疊
    vdur = media_duration(video)
    print(f"\n影片長度 {vdur:.1f}s")
    for i, s in enumerate(segs, 1):
        d = media_duration(work / f"{i:02d}.mp3")
        end = s["t"] + d
        nxt = segs[i]["t"] if i < len(segs) else vdur
        flag = "  ⚠ 超過下一段/片尾" if end > nxt else ""
        print(f"[{i:02d}] {s['t']:>6.1f} → {end:>6.1f}s（{d:.1f}s）{flag}")
    if args.tts_only:
        return

    # 3. 合成：各段 adelay → amix → apad 補到影片長度，原音軌直接取代
    cmd = [FFMPEG, "-nostdin", "-y", "-i", str(video)]
    for i in range(1, len(segs) + 1):
        cmd += ["-i", str(work / f"{i:02d}.mp3")]
    parts = [f"[{i}:a]adelay={int(s['t'] * 1000)}:all=1[a{i}]" for i, s in enumerate(segs, 1)]
    mix_in = "".join(f"[a{i}]" for i in range(1, len(segs) + 1))
    parts.append(f"{mix_in}amix=inputs={len(segs)}:normalize=0:duration=longest,"
                 f"apad=whole_dur={vdur:.3f}[aout]")
    out = video.with_name(video.stem + "_配音.mp4")
    cmd += ["-filter_complex", ";".join(parts), "-map", "0:v", "-map", "[aout]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-t", f"{vdur:.3f}", str(out)]
    r = subprocess.run(cmd, capture_output=True, encoding="utf-8", errors="replace")
    if r.returncode:
        sys.exit(r.stderr[-2000:])
    print(f"\n完成：{out}")


if __name__ == "__main__":
    main()
