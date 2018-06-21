from ThinService.Common import Constants
from ThinService.Server.RequestHandler import RequestHandler
from ThinService.Server.ServerService import ServerService


def printInitMessage():
    print("THINSERVICE SERVER")
    print("Port: %d" % Constants.SERVER_PORT)
    print("=====================")


requestHandler = RequestHandler()
serverService = ServerService(requestHandler)

printInitMessage()

print("Starting server...")
serverService.startServer()
