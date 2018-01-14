# Imports

from bot_class import Bot
from channel_class import Channel
from chat_class import Chat
# Classes
from server_class import Server
from socket_class import Socket
from user_class import User
from viewers_class import Viewers

# Setup Classes
server = "irc.twitch.tv"
port = 6667
svr = Server(server, port)

channel = "metzelrio"
chn = Channel(channel)

user = "grintwisted"
usr = User(user)

bot = "smirksbot"
oath = "oauth:s9cbzfp1bglrisa6aj4rgpmninep16"
bot = Bot(bot, oath)

vws = Viewers(chn)

sck = Socket(svr, chn, bot)
cht = Chat(sck, chn)

# Program
cht.load()
vws.fill_chatlists()
vws.print_chatlist("moderators")
while True:
    cht.chat_loop()