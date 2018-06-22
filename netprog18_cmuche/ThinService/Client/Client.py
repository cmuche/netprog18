import platform

from ThinService.Client.ClientService import ClientConnector
from ThinService.Common import Constants
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

clientConnector = ClientConnector()
try:
    clientConnector.connectToServer()
    print("Successfully connected to the server.")
except:
    print("Could not connect to the server!")

clientConnector.login(getClientInfo())
print("Logged in on the server.")

packages = clientConnector.update()
print(packages)
