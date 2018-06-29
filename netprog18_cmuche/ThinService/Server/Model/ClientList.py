import time

import Constants
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
        self.updateLastSeen(clientId)
        self.logger.log("Registered client with id %d" % clientId)

    def updateLastSeen(self, id):
        timestamp = time.time()
        self.clients[id].lastSeen = timestamp
        self.logger.log("Updated lastSeen for client %d to %d" % (id, timestamp))

    def isClientRegistered(self, id):
        return id in self.clients.keys()

    def getActiveIds(self):
        ret = []
        for client in self.clients:
            if self.isClientActive(self.getClient(client)):
                ret.append(client)
        return ret

    def getClient(self, id):
        return self.clients[id]

    def isClientActive(self, client):
        return client.lastSeen >= (time.time() - Constants.SERVER_LASTSEEN_THRESHOLD)
