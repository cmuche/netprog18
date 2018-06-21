from ThinService.Common.Logger import Logger


class RequestHandler:
    def __init__(self):
        self.logger = Logger("RequestHandler")

    def hello(self, clientId, clientInfo):
        self.logger.logRequest("hello", "id: %d info: %s" % (clientId, clientInfo))