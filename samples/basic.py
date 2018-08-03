# -*- coding: utf-8 -*-
import sys
import os
#import time

sys.path.append("../pyExeManager") # Adds higher directory
from process import Process

# Configuration
FULL_PATH = os.path.dirname(os.path.abspath(__file__))

def abort(message, error_code):
    """ Abort execution with error code """
    print(message)
    sys.exit(error_code)

#def get_current_ms():
#    return int(round(time.time() * 1000))

def main():
    binary_path = os.path.join(FULL_PATH, "../bin/")
    binary_name = "playersample"

    player = Process()
    player.set_up(binary_path, binary_name)
    if not player.create_process():
        abort("Cannot create process, Exiting...", 1)
    player.stdout_until('q. Quit menu')
    player.stdin('3\n')
    player.stdout_until('q. Quit menu')
    player.kill_process()

if __name__ == "__main__":
    main()
