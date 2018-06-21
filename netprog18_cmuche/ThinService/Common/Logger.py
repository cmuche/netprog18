class Logger:
    def __init__(self, senderName):
        self.senderName = senderName

    def log(self, message):
        print("[%s] %s" % (self.senderName, message))

    def logRequest(self, name, message):
        print("[%s] <%s> %s" % (self.senderName, name, message))
