import socket

host='127.0.0.1'
port=5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))

message = s.recv(4096)

while message:
	print("Received:"+message.decode())
	message = s.recv(4096)
	
s.close()
