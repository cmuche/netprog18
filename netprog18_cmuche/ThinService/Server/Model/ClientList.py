from ThinService.Common.Logger import Logger
from ThinService.Server.Model.Client import Client


class ClientList:
    def __init__(self):
        self.logger = Logger("ClientList")
        self.clients = dict()

    def clientRegistered(self, clientId):
        return clientId in self.clients

    def registerClient(self, clientId, clientInfo):
        self.clients[clientId] = Client(clientId, clientInfo)
        self.logger.log("Registered client with id %d" % clientId)

    def getIds(self):
        return self.clients.keys()