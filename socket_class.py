import socket

class Socket:
    def __init__(self, svr, chn, bot):
        self.svr = svr
        self.chn = chn
        self.bot = bot

    def setup(self):
        setup = socket.socket()
        setup.connect((self.svr.__getattr__("server"), self.svr.__getattr__("port")))
        setup.send(("PASS "+self.bot.__getattr__("oath")+"\r\n").encode())
        setup.send(("NICK "+self.bot.__getattr__("bot")+"\r\n").encode())
        setup.send(("JOIN #"+self.chn.__getattr__("channel")+"\r\n").encode())
        return setup