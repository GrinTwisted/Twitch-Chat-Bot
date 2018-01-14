class Bot:
    def __init__(self, bot, oath):
        self.bot = bot
        self.oath = oath

    def __getattr__(self, attr):
        return getattr(self, attr)