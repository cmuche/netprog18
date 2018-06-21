import sys

from netprog18 import ThinService

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


transport = TSocket.TSocket('127.0.0.1', 9090)
transport = TTransport.TBufferedTransport(transport)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = ThinService.Client(protocol)

print("OPENING")
transport.open()

resp = client.foobar()
print("RESPONSE")
print(resp)

transport.close()