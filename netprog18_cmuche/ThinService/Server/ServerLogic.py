from ThinService.Common.Errors.ClientAlreadyRegisteredError import ClientAlreadyRegisteredError
from ThinService.Server.Model.ClientList import ClientList
from ThinService.Common.Logger import Logger
from ThinService.Server.UpdateManager import UpdateManager


class ServerLogic:
    def __init__(self):
        self.logger = Logger("ServerLogic")
        self.clientList = ClientList()
        self.updateManager = UpdateManager()

    def listClients(self):
        self.logger.logRequest("list clients", "")
        return self.clientList.getIds()

    def hello(self, clientId, clientInfo):
        self.logger.logRequest("hello", "id: %d info: %s" % (clientId, clientInfo))
        if self.clientList.isClientRegistered(clientId):
            raise ClientAlreadyRegisteredError()
        else:
            self.clientList.registerClient(clientId, clientInfo)

    def update(self, clientId):
        self.logger.logRequest("update", "id: %d" % clientId)
        return self.updateManager.packages
