class Server:
    def __init__(self, server, port):
        self.server = "irc.twitch.tv"
        self.port = 6667

    def __getattr__(self, attr):
        return getattr(self, attr)