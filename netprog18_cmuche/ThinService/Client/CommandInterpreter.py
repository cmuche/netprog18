import sys

from ThinService.Common.Logger import Logger


class CommandInterpreter:
    def __init__(self, clientService):
        self.logger = Logger("CommandInterpreter")
        self.clientService = clientService

    def executeCommand(self, commandString):
        self.logger.log("Executing command '%s'" % commandString)

        if commandString == "quit":
            self.logger.log("Goodbye.")
            sys.exit()

        try:
            method = getattr(self.clientService, commandString)
            result = method()
            print("Result = %s" % result)
        except:
            self.logger.log("Invalid command!")
