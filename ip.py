import socket

local_ip = socket.gethostbyname(socket.gethostname())
print(local_ip)