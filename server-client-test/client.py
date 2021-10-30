
from socket import AF_INET, SOCK_DGRAM, SOCK_STREAM, socket
import sys


host= "0.0.0.0"
port = 9999
s = socket(AF_INET,SOCK_STREAM)
s.bind((host,port))

addr = (host,port)
buf=4096


def recieve_remder():
    while True:

        data,addr = s.recvfrom(buf)

        if data:

            data,addr = s.recvfrom(buf)
            b2 = 0

            f = open("recv/received.deb",'wb')

            while(data):
                f.write(data)
                s.settimeout(2)
                b2 += buf
                mb = round(b2 / 1024 / 1024, 2)
                sys.stdout.write("\rReceived: "+ str(mb) +" MB")
                sys.stdout.flush()
                data,addr = s.recvfrom(buf)

            break


recieve_remder()