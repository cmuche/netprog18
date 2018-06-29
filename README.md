# netprog18
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
