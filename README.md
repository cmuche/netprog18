# netprog18
The project for the lecture netprog18.

## About this project
This project consist of a server and a client module for a thin client software architecture.
It is written in Python 3 and uses Apache Thrift for communication and API definition.

## How to use

The workspace directory is ```netprog18_cmuche```.
In some cases you have to specify the sources path in your ```PYTHONPATH``` or ```PYTHONHOME``` environment variable.

### Run the modules

#### Server
```python ThinService/Server/Server.py```

#### Client
```python ThinService/Client/Client.py```

### Control the client
...

## Internals

### Client login
...

### Package management
...

## Thrift file
See [this PDF](http://bibiserv.cebitec.uni-bielefeld.de/resources/lehre/netprog18/Projekt-2018.pdf) as an example.
The ```thinservice.thrift``` file defines the API.

```
list<int> listClients()
```
Lists all client IDs which are active at the moment

```
ClientDetails show(1:int clientId) throws (1:InvalidClientId err)
```
Shows details and client (hardware) information für a client id. Throws an exception if the client id is not registered at all. Shows information also for inactive clients

```
void hello(1:int clientId, 2:ClientInfo clientInfo) throws (1:ClientAlreadyRegisteredError err)
```
Registers a client on the server and sends the client hardware info along. Throws an exception if the client id is already registered and the connected client is active. Re-registers the new client if the connected client is inactive

```
void alive(1:int clientId)
```
Updates the lastSeen attribute on the server

```
list<Package> update(1:int clientId)
```
Gets a list of all available packages and their information

```
binary upgrade(1:int clientId, 2:int packageId) throws (1:InvalidPackageId err)
```
Downloads the package archive for the given package id and informs the server about the new package id

## Example usage
### Upgrade and package info
```
[ClientConnector] Client id: 128454772
[Client] Successfully connected to the server.
[Client] Logged in on the server.

Enter command: show 128454772
[CommandInterpreter] Executing command 'show 128454772'
Result = ClientDetails(info=ClientInfo(cpu='Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', gpu='GPU', ram='RAM'), packageId=-1, lastSeen=1530269284)

Enter command: update
[CommandInterpreter] Executing command 'update'
Result = [Package(id=1, name='1.0.0', version=100, checksum='123456789', url=None, date=1529665021, dependency='Python'), Package(id=2, name='1.1.0', version=110, checksum='234567890', url=None, date=1529665031, dependency='Python'), Package(id=3, name='2.0.0', version=200, checksum='345678901', url=None, date=1529665041, dependency='Python')]

Enter command: upgrade 1
[CommandInterpreter] Executing command 'upgrade 1'
[UpgradeManager] Received package from server. File: package-128454772-1.zip
[UpgradeManager] Executing package command: unzip -o -q client-package-tmp/package-128454772-1.zip -d client-package-tmp/package-128454772-1.zip_out
Result = None

Enter command: show 128454772
[CommandInterpreter] Executing command 'show 128454772'
Result = ClientDetails(info=ClientInfo(cpu='Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', gpu='GPU', ram='RAM'), packageId=1, lastSeen=1530269284)
```

### Last seen status and ```list``` filtering
```
[ClientConnector] Client id: 128454772
[Client] Successfully connected to the server.
[Client] Logged in on the server.

Enter command: list
[CommandInterpreter] Executing command 'list'
Result = [128454772]

Enter command: show 128454772
[CommandInterpreter] Executing command 'show 128454772'
Result = ClientDetails(info=ClientInfo(cpu='Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', gpu='GPU', ram='RAM'), packageId=-1, lastSeen=1530269409)

Enter command: list
[CommandInterpreter] Executing command 'list'
Result = []

Enter command: alive
[CommandInterpreter] Executing command 'alive'
Result = None

Enter command: list
[CommandInterpreter] Executing command 'list'
Result = [128454772]

Enter command: show 128454772
[CommandInterpreter] Executing command 'show 128454772'
Result = ClientDetails(info=ClientInfo(cpu='Intel64 Family 6 Model 60 Stepping 3, GenuineIntel', gpu='GPU', ram='RAM'), packageId=-1, lastSeen=1530269431)
```
