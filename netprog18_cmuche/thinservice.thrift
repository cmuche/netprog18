namespace py netprog18

typedef i32 int
typedef i64 long

struct ClientInfo
{
    1: required string cpu;
    2: required string gpu;
    3: required string ram;
}

struct Package
{
    1: required int id;
    2: required string name;
    3: required string version;
    4: required string checksum;
    5: required string url;
    6: required long date;
    7: required string dependency;
}

service ThinService
{
	list<int> listClients()
	ClientInfo show(1:int clientId)
	void hello(1:int clientId, 2:ClientInfo clientInfo)
	void alive(1:int clientId)

	list<Package> update(1:int clientId)
	void upgrade(1:int clientId, 2:int packageId)
}