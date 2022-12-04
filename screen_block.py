from time import sleep
import ctypes
from os import system

def screen_block():
    try:
        system('cls')
        ctypes.windll.kernel32.SetConsoleTitleW("Screen block")
        print('---< Press Ctrl+C to stop >---'.center(80))
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000002)
        while True:
            sleep(60)
    except KeyboardInterrupt:
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000)
        print('Screen block stopped')

if __name__ == '__main__':
    screen_block() 