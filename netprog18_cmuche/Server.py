import Constants
from netprog18 import ThinService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class ThinServiceHandler:
    def hello(self, clientInfo):
        print(clientInfo)


print("CREATING SERVER")
handler = ThinServiceHandler()
processor = ThinService.Processor(handler)
transport = TSocket.TServerSocket(Constants.SERVER_HOST, Constants.SERVER_PORT)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
server.serve()
