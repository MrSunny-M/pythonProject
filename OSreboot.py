import os
import sys

def check_reboot:
    """Returns True if server has a pending restart"""
    return os.path.exist("/run/reboot-required")

def main():
    if check_reboot():
        print("pending restart")
        sys.exit(1)
    print("Everything is fine")
    sys.exit(0)

main()