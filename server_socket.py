import socket


# create socket
ms = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# get address information
ainfo = socket.getaddrinfo(None, 1234)
# print address information to confirm
print(ainfo)
# data at indexes 4 at 4 have the loopback address of machine
print(ainfo[4][4])


# bind the socket to the address of the machine
ms.bind(ainfo[4][4])


# listen for incoming data
ms.listen(5)


# create connection
conn, addr = ms.accept()


# receive data
data = conn.recv(1000)


# print received data
print(data)
