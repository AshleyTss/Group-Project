import socket
import json
from cryptography.fernet import Fernet
import os
import pickle

#Create Socket Object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5000
s.connect((host, port))

# User Input in the Dictionary Data Type
dic3 = dict({1: 'Queen', 2: 'of', 3: 'UK'})
print("\nDictionary with the use of data(): ")

#Serialize the dictionary in JSON format
with open("outfile.json", "w") as outfile:
    json.dump(dic3, outfile)
    filename = '../outfile.json'
print(filename)

# Generate Key for Encryption
key = Fernet.generate_key()

# string the key in a file
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
            
# using the generated key
fernet = Fernet(key)    

# opening the original file to encrypt
with open('outfile.json', 'rb') as file:
    original = file.read()

# encrypting the file
encrypted_text = fernet.encrypt(original)	

# opening the file in write mode and
# writing the encrypted data
with open('outfile2.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_text)	

#Open the file data
file = open('outfile2.txt', "r")
data = file.read()

#Send to the server
while data:
    print("Sending...")
    s.sendall(data.encode())
    data = s.recv(4096)

#Close the connection
s.close()

