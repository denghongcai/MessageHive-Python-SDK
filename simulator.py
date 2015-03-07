#!/usr/bin/python

import message_pb2
from pack import *
from socket import *
from tlslite import TLSConnection

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('server01.dhc.house', 1430))

connection = TLSConnection(sock)
connection.handshakeClientCert()

## Authentication message
msg = message_pb2.Container()
msg.SID = 'a'
msg.RID = 'a'
msg.STIME = 0
msg.TYPE = 0
msg.BODY = '{"token":"foo"}'

data = Packet.Pack(msg)

connection.write(data)

raw_input('Press enter to exit')

connection.close()
