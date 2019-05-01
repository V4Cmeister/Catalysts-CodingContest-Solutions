import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

TCP_IP = "localhost"
TCP_PORT = 7000
BUFFER_SIZE = 1024
MESSAGE = "32"

s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE.encond)
data = s.recv(BUFFER_SIZE)

print("data:", data)