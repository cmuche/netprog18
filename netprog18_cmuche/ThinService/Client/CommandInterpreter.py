import sys

from ThinService.Common.Logger import Logger
from netprog18.ttypes import ClientAlreadyRegisteredError, InvalidClientId, InvalidPackageId


class CommandInterpreter:
    def __init__(self, clientService):
        self.logger = Logger("CommandInterpreter")
        self.clientService = clientService

    def executeCommand(self, commandString):
        """
        Interprets and executes a command string
        :param commandString: The raw command string including parameters
        """
        self.logger.log("Executing command '%s'" % commandString)

        commandParts = commandString.split(" ")

        if commandParts[0] == "quit":
            self.logger.log("Goodbye.")
            sys.exit()

        if commandParts[0] == "hello":
            self.logger.log("Can't execute 'hello' method manually!")
            return

        try:
            method = getattr(self.clientService, commandParts[0])
            params = self.getParamsList(commandParts)
        except:
            self.printError("Invalid command!")
            return

        try:
            result = method(*params)
            print("Result = %s" % result)
        except ClientAlreadyRegisteredError:
            self.printError("A client with the same id is already registered on the server!")
        except InvalidClientId:
            self.printError("This client id does not exist!")
        except InvalidPackageId:
            self.printError("This package id does not exist!")
        except:
            self.logger.log("Error executing command!")
            raise

    def printError(self, err):
        """
        Prints an error
        :param err: The error string
        """
        print("Error = %s" % err)

    def getParamsList(self, commandParts):
        """
        Extracs the parameters of a command and converts them if necessary
        :param commandParts: The parts of the command
        :return: List of parameters
        """
        paramsRaw = commandParts[1:]
        params = []
        for r in paramsRaw:
            try:
                params.append(int(r))
            except:
                params.append(r)
        return params
