import OS

def check_reboot:
    """Returns True if server has a pending restart"""
    return os.path.exists("/run/reboot-required")

def main():
    pass

main()