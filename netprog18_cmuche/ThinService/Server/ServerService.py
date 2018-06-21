from ThinService.Common import Constants

from ThinService.Server.RequestHandler import RequestHandler
from netprog18 import ThinService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer


class ServerService:
    def __init__(self, requestHandler):
        self.requestHandler = requestHandler

    def startServer(self):
        processor = ThinService.Processor(self.requestHandler)
        serverSocket = TSocket.TServerSocket(Constants.SERVER_HOST, Constants.SERVER_PORT)
        transportFactory = TTransport.TBufferedTransportFactory()
        protocolFactory = TBinaryProtocol.TBinaryProtocolFactory()

        server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactory)
        server.serve()
