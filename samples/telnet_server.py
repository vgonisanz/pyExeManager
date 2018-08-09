import gevent, gevent.server
from telnetsrv.green import TelnetHandler, command
import time

import settings

def append_timestamp(msg):
    timestr = time.strftime("[%Y/%m/%d - %H:%M:%S] ")
    return "".join([timestr, msg])

class TelnetHandler(TelnetHandler):
    WELCOME = "Welcome to telnet test server."
    PROMPT = "Server>"

    def session_start(self):
        print("A user has connected!")
        return

    @command(['echo', 'copy', 'repeat'])
    def command_echo(self, params):
        """
        cmd <text to echo>
        Echo text back to the console.
        """
        message = append_timestamp(' '.join(params))
        self.writeresponse( message )
        return

    @command('timer')
    def command_timer(self, params):
        """
        cmd <time> <message>
        In <time> seconds, display <message>.
        Send a message after a delay.
        <time> is in seconds.
        If <message> is more than one word, quotes are required.
        example:
        > TIMER 5 "hello world!"
        """
        try:
            timestr, message = params[:2]
            time = int(timestr)
        except ValueError:
            self.writeerror( "Need both a time and a message" )
            return
        self.writeresponse("Waiting %d seconds..." % time)
        gevent.spawn_later(time, self.writemessage, message)
        return

    @command('info')
    def command_info(self, params):
        """
        Provides some information about the current terminal.
        """
        self.writeresponse( "Username: %s, terminal type: %s" % (self.username, self.TERM) )
        self.writeresponse( "Command history:" )
        for c in self.history:
            self.writeresponse("  %r" % c)

def main():
    print("Launching server at port: %s" % settings.PORT)
    server = gevent.server.StreamServer(("", settings.PORT), TelnetHandler.streamserver_handle)
    print("Listening...")
    server.serve_forever()

if __name__ == "__main__":
    main()
