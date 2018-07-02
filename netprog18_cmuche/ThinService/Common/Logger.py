class Logger:
    def __init__(self, senderName):
        """
        Initializes a logger
        :param senderName: The name of the logging class
        """
        self.senderName = senderName

    def log(self, message):
        """
        Logs a message
        :param message: The message string
        """
        print("[%s] %s" % (self.senderName, message))

    def logRequest(self, name, message):
        """
        Logs a API request
        :param name: The name of the API method
        :param message: The message string
        """
        print("[%s] <%s> %s" % (self.senderName, name, message))
