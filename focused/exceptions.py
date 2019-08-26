class MissingTag(AttributeError):
    def __init__(self, arg):
        self.strerror = arg
        self.args = {arg}
