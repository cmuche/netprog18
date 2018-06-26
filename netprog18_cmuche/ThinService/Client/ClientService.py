import random
import uuid

from ThinService.Common import Constants
from ThinService.Common.Logger import Logger
from netprog18 import ThinService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class ClientService:
    def __init__(self):
        self.logger = Logger("ClientConnector")
        self.id = self.calculateClientId()
        self.logger.log("Client id: %d" % self.id)

    def calculateClientId(self):
        return int(uuid.getnode()/1000000)

    def connectToServer(self):
        self.transport = TSocket.TSocket(Constants.SERVER_HOST, Constants.SERVER_PORT)
        self.transport = TTransport.TBufferedTransport(self.transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = ThinService.Client(protocol)
        self.transport.open()

    def closeConnection(self):
        self.transport.close()

    def list(self):
        return self.client.listClients()

    def show(self, id):
        return self.client.show(id)

    def login(self, clientInfo):
        self.client.hello(self.id, clientInfo)

    def update(self):
        return self.client.update(self.id)
