import bz2


class Message:

    def __init__(self, message: str):
        self.message = message

    def compress(self):
        return bz2.compress(self.message.encode("utf-8"))
