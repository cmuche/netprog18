namespace py netprog18

typedef i32 int

struct ClientInfo
{
    1: required string cpu;
    2: required string gpu;
    3: required string ram;
}

service ThinService
{
	void hello(1:ClientInfo clientInfo)
}