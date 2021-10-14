from time import time
import os, termios, sys, tty

# frames in data
FRAMES = 685

with open('data.sixel') as f:
    data = f.read()
    start = time()
    end = 0

    print(data)

    tattr = termios.tcgetattr(0)
    try:
        tty.setcbreak(termios.TCSADRAIN)
        print('\x1b[6n')
        os.read(0, 1024)
        end = time()
    finally:
        termios.tcsetattr(0, termios.TCSADRAIN, tattr)
    
    duration = end - start
    print(f'\x1b[2J\x1b[H{round(duration, 2)}s ({round(len(data)/duration/1024/1024, 2)} MB/s, {round(685/ duration, 2)} fps)')

