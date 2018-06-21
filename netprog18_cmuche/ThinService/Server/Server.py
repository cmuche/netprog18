from ThinService.Common import Constants
from ThinService.Common.Logger import Logger
from ThinService.Server.RequestHandler import RequestHandler
from ThinService.Server.ServerService import ServerService


def printInitMessage():
    print("THINSERVICE SERVER")
    print("Port: %d" % Constants.SERVER_PORT)
    print("=====================")


logger = Logger("Server")
requestHandler = RequestHandler()
serverService = ServerService(requestHandler)

printInitMessage()

logger.log("Starting server...")
serverService.startServer()
