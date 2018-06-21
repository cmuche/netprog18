from ThinService.Common import Constants
from ThinService.Server.RequestHandler import RequestHandler
from netprog18 import ThinService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

def printInitMessage():
    print("THINSERVICE SERVER")
    print("Port: %d" % Constants.SERVER_PORT)
    print("=====================")

def startServer():
    requestHandler = RequestHandler()
    processor = ThinService.Processor(requestHandler)
    serverSocket = TSocket.TServerSocket(Constants.SERVER_HOST, Constants.SERVER_PORT)
    transportFactory = TTransport.TBufferedTransportFactory()
    protocolFactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TSimpleServer(processor, serverSocket, transportFactory, protocolFactory)
    server.serve()

printInitMessage()
startServer()
