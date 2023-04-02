import subprocess
import time
proc = subprocess.Popen(["python", "stack_overflow_page.py"], stdout=subprocess.PIPE)
out = proc.communicate()[0]
time.sleep(5)
print ("asghar")
print(out.upper())