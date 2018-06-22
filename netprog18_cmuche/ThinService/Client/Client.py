import platform

from ThinService.Client.ClientService import ClientService
from ThinService.Client.CommandInterpreter import CommandInterpreter
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
clientService = ClientService()
try:
    clientService.connectToServer()
    logger.log("Successfully connected to the server.")
except:
    logger.log("Could not connect to the server!")

clientService.login(getClientInfo())
logger.log("Logged in on the server.")

commandInterpreter = CommandInterpreter(clientService)

while 1:
    print()
    command = input("Enter command: ")
    commandInterpreter.executeCommand(command)