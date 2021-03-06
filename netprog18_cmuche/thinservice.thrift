namespace py netprog18

typedef i32 int
typedef i64 long

struct ClientInfo
{
    1: required string cpu;
    2: required string gpu;
    3: required string ram;
}

struct ClientDetails
{
    1: required ClientInfo info;
    2: required int packageId;
    3: required long lastSeen;
}

struct Package
{
    1: required int id;
    2: required string name;
    3: required int version;
    4: required string checksum;
    5: required string url;
    6: required long date;
    7: required string dependency;
}

exception ClientAlreadyRegisteredError
{
}

exception InvalidClientId
{
}

exception InvalidPackageId
{
}

service ThinService
{
	list<int> listClients()
	ClientDetails show(1:int clientId) throws (1:InvalidClientId err)
	void hello(1:int clientId, 2:ClientInfo clientInfo) throws (1:ClientAlreadyRegisteredError err)
	void alive(1:int clientId)

	list<Package> update(1:int clientId)
	binary upgrade(1:int clientId, 2:int packageId) throws (1:InvalidPackageId err)
}