import random
import sys

from ThinService.Common import Constants
from netprog18 import ThinService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


class ClientConnector:
    def __init__(self):
        self.id = random.randint(0, 2147483647)

    def connectToServer(self):
        self.transport = TSocket.TSocket(Constants.SERVER_HOST, Constants.SERVER_PORT)
        self.transport = TTransport.TBufferedTransport(self.transport)
        protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
        self.client = ThinService.Client(protocol)
        self.transport.open()

    def closeConnection(self):
        self.transport.close()

    def login(self, clientInfo):
        self.client.hello(self.id, clientInfo)
