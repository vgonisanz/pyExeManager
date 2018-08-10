import tftpy
import os

import settings

def main():
    CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
    TFTPBOOT_PATH = os.path.abspath(os.path.join(CURRENT_PATH, "../tftpboot/"))

    print("Launching TELNET server at port: %s\nServing path: %s" % (settings.TFTP_PORT, TFTPBOOT_PATH))

    server = tftpy.TftpServer(TFTPBOOT_PATH)
    print("Listening...")
    server.listen(settings.HOST, settings.TFTP_PORT)

if __name__ == "__main__":
    main()
