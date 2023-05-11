import socket
import sys


# create socket
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket")
    sys.exit()


# get host address
try:
    host = socket.gethostbyname("www.uci.edu")
except socket.gaierror:
    print("Failed to get host")
    sys.exit()


mysock.connect((host, 80))
message = bytes("GET / HTTP/1.1\r\n\r\n".encode())


try:
    mysock.sendall(message)
except socket.error:
    print("Failed to send")
    sys.exit()

data = mysock.recv(1000)
print(data)
mysock.close()
