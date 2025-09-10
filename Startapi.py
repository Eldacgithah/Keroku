import subprocess
import time
import os
import sys
import threading

proc = subprocess.Popen(
    ["python3", "-m", "heroku", "--no-web"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

def read_output(p):
    for line in p.stdout:
        print(line, end="")

t = threading.Thread(target=read_output, args=(proc,))
t.start()

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
t.join()

script_path = os.path.abspath(__file__)
try:
    os.remove(script_path)
except:
    pass
