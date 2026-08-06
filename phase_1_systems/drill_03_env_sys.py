import os, sys

def run_diagnostics() -> None:
    print(f"[SYS USER]: {os.getenv("USER")}")
    print(f"[SYS SHELL]: {os.getenv("SHELL", "Unknown")}")

    if "--verbose" in sys.argv:
        print(f"[EXECUTABLE PATH]: {sys.executable}")
        print(f"[PLATFORM TARGET]: {sys.platform}")

    
run_diagnostics()