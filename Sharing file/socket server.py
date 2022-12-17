import socket
import pickle
import os
from cryptography.fernet import Fernet


# Create a socket object
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host='127.0.0.1'
port=5000
    
# Bind and Listen to the Port
s.bind((host, port))
s.listen(4)
print ("Waiting for incoming connection")
c, addr = s.accept()
print ("Got connection from", str(addr))


#Receive file
while True:
   print("Receiving....")
   Received = c.recv(1024).decode()
   print("Done Receiving.")
received.close()

# start receiving the file from the socket
# and writing to the file stream

# key generation
key=Fernet.generate_key()

# opening the key
with open('filekey.key', 'rb') as filekey:
    key=filekey.read()
    print(key)

# using the key
fernet =Fernet(key)

# opening the encrypted file
#with open('Received', 'rb') as enc_file:
encrypted = Received.read()
print(encrypted)

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('outfile3.txt', 'wb') as dec_file:
    dec_file.write(decrypted)

s.close()
c.close()

