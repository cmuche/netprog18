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
        self.logger.logRequest("list clients", "")
        return self.clientList.getIds()

    def show(self, clientId):
        self.logger.logRequest("show client", "id: %d" % clientId)
        if not self.clientList.isClientRegistered(clientId):
            raise InvalidClientId()
        return self.clientList.getClient(clientId).info

    def hello(self, clientId, clientInfo):
        self.logger.logRequest("hello", "id: %d info: %s" % (clientId, clientInfo))
        if self.clientList.isClientRegistered(clientId):
            raise ClientAlreadyRegisteredError()
        else:
            self.clientList.registerClient(clientId, clientInfo)

    def alive(self, clientId):
        self.logger.logRequest("alive", "id: %d" % clientId)
        if not self.clientList.isClientRegistered(clientId):
            raise InvalidClientId()
        self.clientList.updateLastSeen(clientId)

    def update(self, clientId):
        self.logger.logRequest("update", "id: %d" % clientId)
        return self.updateManager.packages

    def upgrade(self, clientId, packageId):
        self.logger.logRequest("upgrade", "id: %d package: %d" % (clientId, packageId))
        fileName = self.updateManager.getPackageFile(packageId)
        with open(fileName, "rb") as file:
            data = file.read()
            return data
