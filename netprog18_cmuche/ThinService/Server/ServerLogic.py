from ThinService.Server.Model.ClientList import ClientList
from ThinService.Common.Logger import Logger


class ServerLogic:
    def __init__(self):
        self.logger = Logger("ServerLogic")
        self.clientList = ClientList()

    def hello(self, clientId, clientInfo):
        self.logger.logRequest("hello", "id: %d info: %s" % (clientId, clientInfo))
        self.clientList.registerClient(clientId, clientInfo)
