#!/usr/bin/env python3
"""
FaMI Manim Video Series - Unified Runner
Sử dụng:
    python run.py 1               # Render Video 1 (chất lượng cao -qh)
    python run.py 2 -ql           # Render Video 2 (chất lượng thấp -ql để test nhanh)
    python run.py 3 --audio       # Chỉ sinh audio TTS cho Video 3
    python run.py --list          # Liệt kê tất cả các video trong series
"""

import os
import sys
import argparse
import subprocess

# Ensure UTF-8 output on Windows consoles to prevent cp1252 crashes
try:
    if sys.stdout.encoding.lower() != "utf-8":
        sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

VIDEOS = {
    "1": {
        "dir": "video_1",
        "script": "video_3_main.py",
        "scene": "LoanDecisionTree",
        "title": "Video 1: Xac suat phe duyet khoan vay (Decision Tree)",
    },
    "2": {
        "dir": "video_2",
        "script": "video_3_main.py",
        "scene": "LoanDecisionTree",
        "title": "Video 2: Kiem soat chat luong san pham (Bien ngau nhien)",
    },
    "3": {
        "dir": "video_3",
        "script": "video_3_main.py",
        "scene": "LoanDecisionTree",
        "title": "Video 3: Toi uu danh muc dau tu (Hiep phuong sai Markowitz)",
    },
    "4": {
        "dir": "video_4",
        "script": "video_3_main.py",
        "scene": "LoanDecisionTree",
        "title": "Video 4: Phat hien diem bat thuong (Outliers & Leverage)",
    },
}

def print_list():
    print("\n--- Danh sach video trong series FaMI ---")
    for key, info in VIDEOS.items():
        print(f"  [{key}] {info['title']} (Folder: {info['dir']})")
    print("\nCach chay vi du:")
    print("  python run.py 1 -ql         # Test nhanh chat luong 480p15")
    print("  python run.py 3             # Render chuan chat luong cao 1080p")
    print("  python run.py 2 --audio     # Tu dong tao giong doc TTS")
    print()

def main():
    parser = argparse.ArgumentParser(description="Trinh chay video Manim cho FaMI series")
    parser.add_argument("video", nargs="?", default=None, help="So thu tu video (1, 2, 3, 4)")
    parser.add_argument("-q", "--quality", choices=["l", "m", "h", "k"], default="h",
                        help="Chat luong render: l (480p15), m (720p30), h (1080p60), k (4K). Mac dinh: h")
    parser.add_argument("-ql", action="store_const", const="l", dest="quality", help="Render nhanh chat luong thap")
    parser.add_argument("-qm", action="store_const", const="m", dest="quality", help="Render chat luong trung binh")
    parser.add_argument("-qh", action="store_const", const="h", dest="quality", help="Render chat luong cao")
    parser.add_argument("-qk", action="store_const", const="k", dest="quality", help="Render 4K")
    parser.add_argument("--flush_cache", action="store_true", help="Lam sach cache Manim sau khi render")
    parser.add_argument("--audio", action="store_true", help="Chi sinh audio TTS ma khong render video")
    parser.add_argument("--list", action="store_true", help="Liet ke danh sach video")

    args, extra_args = parser.parse_known_args()

    if args.list or not args.video:
        print_list()
        return

    if args.video not in VIDEOS:
        print(f"[!] Khong tim thay video so '{args.video}'.")
        print_list()
        sys.exit(1)

    info = VIDEOS[args.video]
    target_dir = os.path.join(ROOT_DIR, info["dir"])
    if not os.path.exists(target_dir):
        print(f"[!] Thu muc {target_dir} khong ton tai!")
        sys.exit(1)

    print(f"\n=======================================================")
    print(f"[*] Bat dau xu ly: {info['title']}")
    print(f"[*] Thu muc: {target_dir}")
    print(f"=======================================================\n")

    if args.audio:
        cmd = [sys.executable, info["script"]]
    else:
        quality_flag = f"-q{args.quality}"
        cmd = [sys.executable, "-m", "manim", quality_flag]
        if args.flush_cache:
            cmd.append("--flush_cache")
        cmd.extend([info["script"], info["scene"]])
        cmd.extend(extra_args)

    print(f"Chay lenh: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=target_dir)
    sys.exit(result.returncode)

if __name__ == "__main__":
    main()
