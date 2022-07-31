import os
import subprocess
import time
def check():
    checkv = str(subprocess.check_output("tasklist | FINDSTR xserver.exe || echo false", shell=True))
    print(checkv)
    if "false" in checkv:
        return "Closed"
    else:
        return "Open"
while True:
    time.sleep(1)
    if check() == "Closed":
        time.sleep(30)
        os.startfile('xserver.exe')
        os._exit(0)