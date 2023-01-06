import bz2


class Message:

    def __init__(self, message: bytes):
        self.message = message

    def decompress(self):
        return bz2.decompress(self.message)
