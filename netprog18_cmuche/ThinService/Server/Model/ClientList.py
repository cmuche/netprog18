import time

import Constants
from ThinService.Common.Logger import Logger
from ThinService.Server.Model.Client import Client
from netprog18.ttypes import ClientDetails


class ClientList:
    def __init__(self):
        self.logger = Logger("ClientList")
        self.clients = dict()

    def registerClient(self, clientId, clientInfo):
        """
        Registers a new client or replaces the current
        :param clientId: The new client id
        :param clientInfo: Client's hardware information
        """
        self.clients[clientId] = Client(clientId, clientInfo)
        self.logger.log("Registered client with id %d" % clientId)
        self.updateLastSeen(clientId)

    def updateLastSeen(self, id):
        """
        Sets the lastSeen information for a client to the current timestamp
        :param id: The client id
        """
        timestamp = int(time.time())
        self.clients[id].lastSeen = timestamp
        self.logger.log("Updated lastSeen for client %d to %d" % (id, timestamp))

    def updateCurrentPackage(self, id, packageId):
        """
        Updates the information about the installed package for a client
        :param id: The client id
        :param packageId: The package id
        """
        self.clients[id].currentPackage = packageId
        self.logger.log("Updated currentPackage for client %d to %d" % (id, packageId))

    def isClientRegistered(self, id):
        """
        Checks if a client is registeres
        :param clientId: The client id to check
        :return: Boolean value
        """
        return id in self.clients.keys()

    def getActiveIds(self):
        """
        Lists the ids of the active clients
        :return: List of ids
        """
        ret = []
        for client in self.clients:
            if self.isClientActive(self.getClient(client)):
                ret.append(client)
        return ret

    def getClient(self, id):
        """
        Gets information about a client
        :param id: The client id
        :return: The Client object
        """
        return self.clients[id]

    def getClientDetails(self, id):
        """
        Builds a ClientDetails object
        :param id: The client id
        :return: The filled ClientDetails object
        """
        client = self.getClient(id)

        details = ClientDetails()
        details.info = client.info
        details.lastSeen = client.lastSeen
        details.packageId = client.currentPackage
        return details

    def isClientActive(self, client):
        """
        Checks if a client is active
        :param client: The client id
        :return: Boolean value
        """
        return client.lastSeen >= (int(time.time()) - Constants.SERVER_LASTSEEN_THRESHOLD)
