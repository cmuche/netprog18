import time

import Constants
from ThinService.Common.Logger import Logger
from ThinService.Server.Model.Client import Client
from netprog18.ttypes import ClientDetails


class ClientList:
    def __init__(self):
        self.logger = Logger("ClientList")
        self.clients = dict()

    def clientRegistered(self, clientId):
        return clientId in self.clients

    def registerClient(self, clientId, clientInfo):
        self.clients[clientId] = Client(clientId, clientInfo)
        self.logger.log("Registered client with id %d" % clientId)
        self.updateLastSeen(clientId)

    def updateLastSeen(self, id):
        timestamp = int(time.time())
        self.clients[id].lastSeen = timestamp
        self.logger.log("Updated lastSeen for client %d to %d" % (id, timestamp))

    def updateCurrentPackage(self, id, packageId):
        self.clients[id].currentPackage = packageId
        self.logger.log("Updated currentPackage for client %d to %d" % (id, packageId))

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

    def getClientDetails(self, id):
        client = self.getClient(id)

        details = ClientDetails()
        details.info = client.info
        details.lastSeen = client.lastSeen
        details.packageId = client.currentPackage
        return details

    def isClientActive(self, client):
        return client.lastSeen >= (int(time.time()) - Constants.SERVER_LASTSEEN_THRESHOLD)
