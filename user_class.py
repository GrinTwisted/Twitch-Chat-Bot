class User:
    def __init__(self, user):
        self.user = user

    def __getattr__(self, attr):
        return getattr(self, attr)