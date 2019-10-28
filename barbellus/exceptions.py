class Error(Exception):
    pass

class InvalidWeight(Error):
    def __init__(self, message):
        self.message = message
