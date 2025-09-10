import subprocess
import time
import os
import sys
import signal

proc = subprocess.Popen(
    ["python3", "-m", "heroku", "--no-web"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

time.sleep(10)
proc.stdin.write("N\n")
proc.stdin.flush()
time.sleep(7)
proc.stdin.write("20045757\n")
proc.stdin.flush()
time.sleep(5)
proc.stdin.write("7d3ea0c0d4725498789bd51a9ee02421\n")
proc.stdin.flush()

proc.wait()

script_path = os.path.abspath(__file__)
pid = os.getpid()

def remove_self():
    try:
        os.remove(script_path)
    except:
        pass

import threading
t = threading.Thread(target=remove_self)
t.start()

os.kill(pid, signal.SIGTERM)
