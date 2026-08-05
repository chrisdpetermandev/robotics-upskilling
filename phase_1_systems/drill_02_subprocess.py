import subprocess

# Execute System Command: Using subprocess.run()
def run_system_process(process_string) -> None:
    call_keys = process_string.split(" ")
    try:
        process_details = subprocess.run(call_keys, capture_output=True, text=True, check=True)
        print(f"[PROCESS KEYS]: {call_keys}")
        print(f"[PROCESS OUTPUT]: {process_details.stdout.strip()}")
        print(f"[PROCESS RETURN CODE]: {process_details.returncode}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Calling {call_keys} - {e}")

run_system_process("uname -a")
run_system_process("df -h /")