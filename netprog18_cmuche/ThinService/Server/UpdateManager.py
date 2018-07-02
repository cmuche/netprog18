import json

from ThinService.Common.Logger import Logger
from netprog18.ttypes import Package, InvalidPackageId


class UpdateManager:
    def __init__(self):
        self.logger = Logger("UpdateManager")
        self.packages = []
        with open("Resources/packages.json") as f:
            data = json.load(f)
            self.parsePackages(data)
        self.logger.log("Found %d package(s)" % len(self.packages))

    def getPackageById(self, packageId):
        """
        Gets a package, raises an error if the package does not exist
        :param packageId: The package id
        :return: The Package object
        """
        for p in self.packages:
            if p.id == packageId:
                return p
        raise InvalidPackageId()

    def getPackageFile(self, packageId):
        """
        Gets the file name for a package
        :param packageId: The package id
        :return: File name as a string
        """
        package = self.getPackageById(packageId)
        return "Packages/%d.zip" % package.id

    def parsePackages(self, jsonData):
        """
        Parses the package JSON file
        :param jsonData: The JSON string
        :return: A list of Package objects
        """
        for jsonPackage in jsonData:
            package = Package()
            package.id = jsonPackage["id"]
            package.name = jsonPackage["name"]
            package.version = jsonPackage["version"]
            package.checksum = jsonPackage["checksum"]
            package.date = jsonPackage["date"]
            package.dependency = jsonPackage["dependency"]
            self.packages.append(package)