# -*- coding: utf-8 -*-

import sys
import os
import signal
import subprocess
import time

# Configuration
BIN_NAME = "playersample"
FULL_PATH = os.path.dirname(os.path.abspath(__file__))

# Variables
proc = None

class bcolors:
    """ Helper class to define ANSI escape sequences to print with color """
    HEADER = '\033[95m'
    NORMAL = '\033[39m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def abort(message, error_code):
    """ Abort execution with error code """
    print(message)
    sys.exit(error_code)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    clean_up()
    sys.exit(0)

def set_up():
    """
    Initialize variables, signals and working directory
    """

    print("Initializing...")

    signal.signal(signal.SIGINT, signal_handler)
    BIN_PATH = os.path.abspath(os.path.join(FULL_PATH, "../bin/"))
    print("Setting working directory to binary path:", BIN_PATH)
    os.chdir(BIN_PATH)
    return

def clean_up():
    print(bcolors.ENDC)
    print("Cleaning up...")

    return

def get_current_ms():
    return int(round(time.time() * 1000))

def create_process():
    """
    Create process with standard output and error open.
    """
    try:
        global proc
        proc = subprocess.Popen(["./" + BIN_NAME], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        abort("File do not exist, Exiting...", 1)
    print("Process created with pid:", proc.pid)
    return


def stdout_until(end="EOF"):
    """
    Print all output in buffer until end string is found
        * This call will block if end is not found!
    """
    print("stdout sent from last time until end:", end)
    print(bcolors.OKBLUE)

    for line in iter(proc.stdout.readline, ""):
        str_line = line.rstrip().decode('utf-8')
        print("\t> " + str_line)
        if end in str_line:
            break;

    print(bcolors.NORMAL)
    return

def stdin(message):
    """
    Send string to stdin as bytearray and flush the data. No add return carriage so is required to send it
    """
    proc.stdin.write(message.encode())
    proc.stdin.flush()
    return

def kill_process():
    proc.kill()
    outs, errs = proc.communicate()
    print("Process ended with return code:", proc.returncode)
    return

def main():
    set_up()
    create_process()
    stdout_until('q. Quit menu')
    stdin('3\n')
    stdout_until('q. Quit menu')
    kill_process()

if __name__ == "__main__":
    main()
