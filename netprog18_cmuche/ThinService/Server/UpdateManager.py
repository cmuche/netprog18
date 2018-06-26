import json

from ThinService.Common.Logger import Logger
from netprog18.ttypes import Package


class UpdateManager:
    def __init__(self):
        self.logger = Logger("UpdateManager")
        self.packages = []
        with open("Resources/packages.json") as f:
            data = json.load(f)
            self.parsePackages(data)
        self.logger.log("Found %d package(s)" % len(self.packages))

    def parsePackages(self, jsonData):
        for jsonPackage in jsonData:
            package = Package()
            package.id = jsonPackage["id"]
            package.name = jsonPackage["name"]
            package.version = jsonPackage["version"]
            package.checksum = jsonPackage["checksum"]
            package.date = jsonPackage["date"]
            package.dependency = jsonPackage["dependency"]
            self.packages.append(package)