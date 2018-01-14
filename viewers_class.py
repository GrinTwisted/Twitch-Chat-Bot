from urllib.request import urlopen
from json import loads

class Viewers:
    def __init__(self, chn):
        self.chn = chn
        self.moderators = []
        self.staff = []
        self.admins = []
        self.global_mods = []
        self.viewers = []

    def fill_chatlists(self):
        self.response = urlopen('https://tmi.twitch.tv/group/user/'
                                +self.chn.__getattr__("channel")+
                                '/chatters')
        self.readable = self.response.read().decode('utf-8')
        chatlist = loads(self.readable)
        chatters = chatlist['chatters']
        for role in chatters:
            setattr(self, role, chatters[role])

    def print_chatlist(self, viewer_type):
            print(getattr(self, viewer_type))