import socket

host='127.0.0.1'
port=5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)

c, addr = s.accept()

print ("Got connection from", str(addr))
	
c.send(b"Hello from Server")

note = "Thank you for connecting"

c.send(note.encode())

c.close()
