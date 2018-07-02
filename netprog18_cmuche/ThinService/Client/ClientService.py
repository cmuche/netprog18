import uuid

from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket
from thrift.transport import TTransport

from ThinService.Common import Constants
from ThinService.Common.Logger import Logger
from UpgradeManager import UpgradeManager
from netprog18 import ThinService


class ClientService:
    def __init__(self):
        self.logger = Logger("ClientConnector")
        self.id = self.calculateClientId()
        self.upgradeManager = UpgradeManager()
        self.logger.log("Client id: %d" % self.id)

    def calculateClientId(self):
        """
        Calculated a unique hardware id
        :return: The id as an integer
        """
        return int(uuid.getnode() / 1000000)

    def connectToServer(self):
        """
        Sets up the server connection and opens it
        """
        self.transport = TSocket.TSocket(Constants.SERVER_HOST, Constants.SERVER_PORT)
        self.transport = TTransport.TBufferedTransport(self.transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = ThinService.Client(protocol)
        self.transport.open()

    def closeConnection(self):
        """
        Closes the server connection
        """
        self.transport.close()

    def list(self):
        """
        Lists all active clients
        :return: List of client ids
        """
        return self.client.listClients()

    def show(self, id):
        """
        Shows client information
        :param id: The client id
        :return: A ClientDetails object
        """
        return self.client.show(id)

    def login(self, clientInfo):
        """
        Registers the client on the server
        :param clientInfo: The client's hardware information
        """
        self.client.hello(self.id, clientInfo)

    def alive(self):
        """
        Updates the lastSeen information on the server
        """
        self.client.alive(self.id)

    def update(self):
        """
        Gets information about available packages
        :return: A list of package information
        """
        return self.client.update(self.id)

    def upgrade(self, packageId):
        """
        Downloads a package and installs it
        :param packageId: The package id
        """
        data = self.client.upgrade(self.id, packageId)
        self.upgradeManager.applyUpgrade(self.id, packageId, data)
