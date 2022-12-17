import socket
import os
import json
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

#Start receiving the file from the socket
content = c.recv(4096).decode()
print("Done Receiving.")

#write data to a file
received= open('outfile3.txt',"w")
received.write(content)
received.close()

#Decryption
# opening the key
if os.path.exists('filekey.key'):
    filekey=open('filekey.key', 'rb')
    key=filekey.read()
    filekey.close()

# using the key
fernet =Fernet(key)

#openign the encrypted file
with open('outfile3.txt','rb') as enc_file:
    encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('outfile4.txt', 'wb') as dec_file:
    dec_file.write(decrypted)
    print("Decrypted File: ", decrypted)
    print(type(decrypted))


with open('outfile4.txt',"rb") as infile:
    dic3_recover=json.load(infile)
    print("Reconstructed decrypted", dic3_recover)
    print(type(dic3_recover))

c.close()

