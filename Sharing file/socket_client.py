import socket
import pickle
import json
from cryptography.fernet import Fernet
import os


class Client:
    # This class connects the Client to Server and send the files both in Encrypted and Decrypted Form
	
    ## to be updated ##

    def __init__(self):
        # Socket to connect to Server
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_to_server(self):
        # Standard loopback interface address (localhost)
        host = '127.0.0.1'
        port = 5000
        self.s.connect((host, port))
        message = self.s.recv(4096)
		
        while message:
                print("Received:"+message.decode())
        message = self.s.recv(4096)

    def disconnect_server(self):
            self.s.close()  # To disconnect client from server

    def dict(self):

            # User Input in the Dictionary Data Type
            dic3 = dict({1: 'Queen', 2: 'of', 3: 'UK'})
            print("\nDictionary with the use of dic3(): ")
            
            #Serialize the dictionary in JSON format
            with open("test.pickle", "w") as outfile:
                pickle.dump(dic3, outfile)
            print("Written dictionary", dic3)
       
    def encrypt(self):
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
            with open('file.txt', 'rb') as file:
                original = file.read()

            # encrypting the file
            encrypted = fernet.encrypt(original)	
                
            # opening the file in write mode and
            # writing the encrypted data
            with open('file2.txt', 'wb') as encrypted_file:
                encrypted_file.write(encrypted)	

    def send_data_to_server(self):
                self.s.send(self.encrypted_output).encode()
                with open(self.encrypted_filename, "rb") as file:
                    dic3 = file.read(4096)
                    while dic3:
                        self.s.send(dic3)
                        dic3 = file.read(4096)
                print("Sent Successfully")

if __name__ == "__main__":

    client = Client()
    # To Connect Client with Server
    client.connect_to_server()
    # Disconnect Server
    client.disconnect_server()