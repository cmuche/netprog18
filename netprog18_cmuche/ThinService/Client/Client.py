import platform

from ThinService.Client.ClientService import ClientConnector
from ThinService.Common import Constants
from ThinService.Common.Logger import Logger
from netprog18.ttypes import ClientInfo


def getClientInfo():
    clientInfo = ClientInfo()
    clientInfo.cpu = platform.processor()
    clientInfo.gpu = "GPU"
    clientInfo.ram = "RAM"
    return clientInfo


def printInitMessage():
    print("THINSERVICE CLIENT")
    print("Host: %s" % Constants.SERVER_HOST)
    print("Port: %d" % Constants.SERVER_PORT)
    print("Client Info: %s" % getClientInfo())
    print("=====================")


printInitMessage()

logger = Logger("Client")
clientConnector = ClientConnector()
try:
    clientConnector.connectToServer()
    logger.log("Successfully connected to the server.")
except:
    logger.log("Could not connect to the server!")

clientConnector.login(getClientInfo())
logger.log("Logged in on the server.")

packages = clientConnector.update()
print(packages)
