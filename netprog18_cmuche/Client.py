import platform

import Constants
from netprog18 import ThinService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from netprog18.ttypes import ClientInfo


def getClientInfo():
    clientInfo = ClientInfo()
    clientInfo.cpu = platform.processor()
    clientInfo.gpu = "GPU"
    clientInfo.ram = "RAM"
    return clientInfo


transport = TSocket.TSocket(Constants.SERVER_HOST, Constants.SERVER_PORT)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = ThinService.Client(protocol)

print("OPENING")
transport.open()

clientInfo = getClientInfo()
client.hello(clientInfo)

transport.close()
