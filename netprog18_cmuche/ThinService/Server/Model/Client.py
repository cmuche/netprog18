class Client:
    def __init__(self, id, info):
        self.id = id
        self.info = info
        self.lastSeen = -1
        self.currentPackage = -1