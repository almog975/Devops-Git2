import socket
import os
import getpass

def show_sysinfo():
    print("\n===== System Information =====")
    print(f"Hostname         : {socket.gethostname()}")
    print(f"Current User     : {getpass.getuser()}")
    print(f"Working Directory: {os.getcwd()}")
    print("=" * 30)
