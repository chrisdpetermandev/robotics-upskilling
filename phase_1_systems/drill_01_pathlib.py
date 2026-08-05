from pathlib import Path
from typing import Iterator

def get_parent_directory() -> Path:
    log_dir = Path.home() / "Desktop" / "Robotics-Upskilling"
    if log_dir.exists():
        return log_dir
    else:
        raise FileNotFoundError(f"Target directory does not exist:{log_dir}")
        

def scan_markdown_files(log_dir: Path) -> None:
    try:
        markdown_files = log_dir.rglob("*.md")

        for markdown_file in markdown_files:
            print(f"FILE NAME: {markdown_file.name}")
            print(f"FILE PARENT: {markdown_file.parent.name}")
            print(f"FILE SIZE(BYTES): {markdown_file.stat().st_size}")
    except Exception as e:
        print(f"[ERROR]: Could not locate .md files\n[MESSAGE]{e}")


log_file = get_parent_directory()
scan_markdown_files(log_file)