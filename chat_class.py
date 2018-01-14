import socket

class Chat:
    def __init__(self, sck, chn):
        self.sck = sck.setup()
        self.chn = chn

    def load(self):
        loading = True
        while loading:
            read = self.sck.recv(1024).decode()
            temp = read.split("\n")
            temp.pop()
            for line in temp:
                loading = self.load_complete(line)
        print("Bot has Joined Channel : ", self.chn.__getattr__("channel"))

    def load_complete(self, line):
        if ("End of /NAMES list" in line):
            return False
        else:
            return True

    def get_user(self, line):
        sep = line.split(":", 2)
        return sep[1].split("!", 1)[0]

    def get_message(self, line):
        try: return (line.split(":", 2))[2]
        except: return ""

    def send_message(self, message):
        self.sck.send(("PRIVMSG #"+self.chn.__getattr__("channel")+
                       " :"+message+"\r\n").encode())

    # Returns True if it is the Twitch Server
    def check_console(self, line):
        if "PRIVMSG" in line: return False
        else: return True

    def chat_loop(self):
        try:
            read = self.sck.recv(1024).decode()
            temp = read.split("\n")
        except: temp = ""
        for line in temp:
            if line == "": break
            elif "PING" in line and self.check_console(line):
                self.sck.send("PONG tmi.twitch.tv\r\n".encode())
            user = self.get_user(line)
            message = self.get_message(line)
            print(user, " > ", message)