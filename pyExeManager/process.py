# -*- coding: utf-8 -*-
import os
import sys
import signal
import subprocess

from bcolors import bcolors

class Process(object):
    # Variables
    proc = None
    binary_path = ""
    binary_name = ""

    def __init__(self):
        return

    def signal_handler(self, sig, frame):
        print('You pressed Ctrl+C!')
        self.clean_up()
        sys.exit(0)

    def set_up(self, working_path, binary_name):
        """
        Initialize variables, signals and working directory
        """

        print("Initializing...")
        signal.signal(signal.SIGINT, self.signal_handler)
        self.binary_path = os.path.abspath(working_path)
        self.binary_name = binary_name
        return

    def clean_up(self):
        print(bcolors.ENDC)
        print("Cleaning up...")
        return

    def create_process(self):
        """
        Create process with standard output and error open.
        return: If success
        """
        print("Setting working directory to binary path:", self.binary_path)
        os.chdir(self.binary_path)
        try:
            FULL_BINARY_PATH = os.path.join(self.binary_path, self.binary_name)
            print("Executing:", FULL_BINARY_PATH)
            self.proc = subprocess.Popen([FULL_BINARY_PATH], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except FileNotFoundError:
            return False
        print("Process created with pid:", self.proc.pid)
        return True

    def stdout_until(self, end="EOF"):
        """
        Print all output in buffer until end string is found
            * This call will block if end is not found!
        """
        print("stdout sent from last time until end:", end)
        print(bcolors.OKBLUE)

        for line in iter(self.proc.stdout.readline, ""):
            str_line = line.rstrip().decode('utf-8')
            print("\t> " + str_line)
            if end in str_line:
                break;

        print(bcolors.NORMAL)
        return

    def stdin(self, message):
        """
        Send string to stdin as bytearray and flush the data. No add return carriage so is required to send it
        """
        self.proc.stdin.write(message.encode())
        self.proc.stdin.flush()
        return

    def kill_process(self):
        """
        Kill the process and print return code
        """
        self.proc.kill()
        outs, errs = self.proc.communicate()
        print("Process ended with return code:", self.proc.returncode)
        return
