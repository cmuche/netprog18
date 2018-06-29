import os

from Common.Logger import Logger
from ThinService.Common import Constants


class UpgradeManager:
    def __init__(self):
        self.logger = Logger("UpgradeManager")

    def applyUpgrade(self, clientId, packageId, data):
        if not os.path.exists(Constants.CLIENT_PACKAGE_DIR):
            os.makedirs(Constants.CLIENT_PACKAGE_DIR)

        fileName = "package-%d-%d.zip" % (clientId, packageId)
        file = open("%s/%s" % (Constants.CLIENT_PACKAGE_DIR, fileName), "wb")
        file.write(data)
        file.close()
        self.logger.log("Received package from server. File: %s" % fileName)

        command = Constants.CLIENT_PACKAGE_COMMAND.replace("[dir]", Constants.CLIENT_PACKAGE_DIR)
        command = command.replace("[package]", fileName)
        self.logger.log("Executing package command: %s" % command)
        os.system(command)
