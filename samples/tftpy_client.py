import tftpy

import settings

session_timeout = 3

def main():
    client = tftpy.TftpClient(settings.HOST, settings.TFTP_PORT)
    client.download(settings.SAMPLE_FILE, settings.SAMPLE_FILE, timeout=session_timeout)
    return

if __name__ == "__main__":
    main()
