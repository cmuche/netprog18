from ThinService.Server.Model.ClientList import ClientList
from ThinService.Common.Logger import Logger
from ThinService.Server.UpdateManager import UpdateManager
from netprog18.ttypes import InvalidClientId, ClientAlreadyRegisteredError


class ServerLogic:
    def __init__(self):
        self.logger = Logger("ServerLogic")
        self.clientList = ClientList()
        self.updateManager = UpdateManager()

    def listClients(self):
        """
        Lists all active clients
        :return: List of client ids
        """
        self.logger.logRequest("list clients", "")
        return self.clientList.getActiveIds()

    def show(self, clientId):
        """
        Shows client information
        :param clientId: The client id
        :return: A ClientDetails object
        """
        self.logger.logRequest("show client", "id: %d" % clientId)
        if not self.clientList.isClientRegistered(clientId):
            raise InvalidClientId()
        return self.clientList.getClientDetails(clientId)

    def hello(self, clientId, clientInfo):
        """
        Registers a client, raises an error if an active client is already registered for the client id
        :param clientId: The client id
        :param clientInfo: The client's hardware information
        """
        self.logger.logRequest("hello", "id: %d info: %s" % (clientId, clientInfo))
        if self.clientList.isClientRegistered(clientId):
            if self.clientList.isClientActive(self.clientList.getClient(clientId)):
                raise ClientAlreadyRegisteredError()
            else:
                self.logger.log("Re-registering client with id %d" % clientId)

        self.clientList.registerClient(clientId, clientInfo)

    def alive(self, clientId):
        """
        Updates the lastSeen information
        :param clientId: The client id
        """
        self.logger.logRequest("alive", "id: %d" % clientId)
        if not self.clientList.isClientRegistered(clientId):
            raise InvalidClientId()
        self.clientList.updateLastSeen(clientId)

    def update(self, clientId):
        """
        Gets information about available packages
        :param clientId: The client id
        :return: A list of package information
        """
        self.logger.logRequest("update", "id: %d" % clientId)
        return self.updateManager.packages

    def upgrade(self, clientId, packageId):
        """
        Gets the binary package file contents
        :param clientId: The client id
        :param packageId: The package id
        :return: The binary string
        """
        self.logger.logRequest("upgrade", "id: %d package: %d" % (clientId, packageId))

        fileName = self.updateManager.getPackageFile(packageId)
        self.clientList.updateCurrentPackage(clientId, packageId)
        with open(fileName, "rb") as file:
            data = file.read()
            return data
