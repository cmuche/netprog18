#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class ClientInfo(object):
    """
    Attributes:
     - cpu
     - gpu
     - ram
    """


    def __init__(self, cpu=None, gpu=None, ram=None,):
        self.cpu = cpu
        self.gpu = gpu
        self.ram = ram

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.cpu = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.gpu = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.ram = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('ClientInfo')
        if self.cpu is not None:
            oprot.writeFieldBegin('cpu', TType.STRING, 1)
            oprot.writeString(self.cpu.encode('utf-8') if sys.version_info[0] == 2 else self.cpu)
            oprot.writeFieldEnd()
        if self.gpu is not None:
            oprot.writeFieldBegin('gpu', TType.STRING, 2)
            oprot.writeString(self.gpu.encode('utf-8') if sys.version_info[0] == 2 else self.gpu)
            oprot.writeFieldEnd()
        if self.ram is not None:
            oprot.writeFieldBegin('ram', TType.STRING, 3)
            oprot.writeString(self.ram.encode('utf-8') if sys.version_info[0] == 2 else self.ram)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.cpu is None:
            raise TProtocolException(message='Required field cpu is unset!')
        if self.gpu is None:
            raise TProtocolException(message='Required field gpu is unset!')
        if self.ram is None:
            raise TProtocolException(message='Required field ram is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(ClientInfo)
ClientInfo.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'cpu', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'gpu', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'ram', 'UTF8', None, ),  # 3
)
fix_spec(all_structs)
del all_structs