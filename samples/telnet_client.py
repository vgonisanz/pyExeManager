import telnetlib
import time

import settings

tn = None
session_timeout = 3 # 120

user = ""
password = ""

def check_response(response):
    if response == b'':
        print("Got empty response")
        tear_down(1)
    return

def tear_down(error_code):
    print("Closing connection...")
    tn.close()
    exit(error_code)
    return

def eof_detected(error):
    print("%s" % error)
    tear_down(2)
    return

def wait_for_prompt():
    try:
        #response = tn.read_very_eager()
        response = tn.read_until(b"Server>", session_timeout)
    except EOFError as e:
        eof_detected(e) # The connection is closed and no cooked data is available
    return str(response)

def main():
    global tn
    print("Connecting to %s:%s" % (str(settings.HOST), str(settings.PORT)))
    tn = telnetlib.Telnet(settings.HOST, settings.PORT)
    time.sleep(1)

    try:
        #response = tn.read_very_eager()
        response = tn.read_until(b"Welcome to telnet test server", session_timeout)
    except EOFError as e:
        eof_detected(e) # The connection is closed and no cooked data is available

    print("Located welcome message, waiting for prompt")

    try:
        #response = tn.read_very_eager()
        response = tn.read_until(b"Welcome to telnet test server", session_timeout)
    except EOFError as e:
        eof_detected(e) # The connection is closed and no cooked data is available

    response = wait_for_prompt()
    print("Prompt found, testing...")

    tn.write(b"help")
    time.sleep(1)
    response = wait_for_prompt()
    print("help return: %s" % response)
    tear_down(0)

if __name__ == "__main__":
    main()
