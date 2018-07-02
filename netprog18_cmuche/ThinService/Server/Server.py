from ThinService.Common import Constants
from ThinService.Common.Logger import Logger
from ThinService.Server.ServerLogic import ServerLogic
from ThinService.Server.ServerService import ServerService


def printInitMessage():
    """
    Prints the welcome message
    """
    print("THINSERVICE SERVER")
    print("Port: %d" % Constants.SERVER_PORT)
    print("=====================")

printInitMessage()

logger = Logger("Server")
serverLogic = ServerLogic()
serverService = ServerService(serverLogic)

logger.log("Starting server...")
serverService.startServer()
