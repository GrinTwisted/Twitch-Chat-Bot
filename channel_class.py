class Channel:
    def __init__(self, channel):
        self.channel = channel

    def __getattr__(self, attr):
        return getattr(self, attr)