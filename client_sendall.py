import socket


# create socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# connect to ip addresss and port number and passing a tuple as the argument for the connect method
# in this case using local machine loopback address
my_socket.connect(("127.0.0.1", 4321))


# send a message
# b converts the str data into a byte-like data
my_socket.sendall(b"hello world")

