import socket
import json
from cryptography.fernet import Fernet
import os


class Client:
    # This class connects the Client to Server and send the files both in Encrypted and Decrypted Form
	
    ## to be updated ##

    def __init__(self):
        # Socket to connect to Server
        self.data = dict()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.filename = ""
        self.original= ""
        self.key_filename = '../key.key'
        self.encrypted_filename = ""
        self.encrypted_text=""


    def connect_server(self):
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
            self.data = dict({1: 'Queen', 2: 'of', 3: 'UK'})
            print("\nDictionary with the use of self.data(): ")
            
            #Serialize the dictionary in JSON format
            with open("outfile.json", "w") as outfile:
                json.dump(self.data, outfile)
                self.filename = '../outfile.json'
            print(self.filename)
       
    def encrypt(self):
            # Generate Key for Encryption
            key = Fernet.generate_key()

            # string the key in a file
            with open(self.key_filename, 'wb') as filekey:
                filekey.write(key)

            # opening the key
            with open(self.key_filename, 'rb') as filekey:
                key = filekey.read()
                        
            # using the generated key
            fernet = Fernet(key)    

            # opening the original file to encrypt
            with open('outfile.json', 'rb') as file:
                self.original = file.read()

            # encrypting the file
            self.encrypted_text = fernet.encrypt(self.original)	
    
            # opening the file in write mode and
            # writing the encrypted data
            with open(self.encrypted_filename, 'wb') as encrypted_file:
                encrypted_file.write(self.encrypted_text)	

    def send_data_to_server(self):
                self.s.send(self.encrypted_filename.encode())
                with open(self.encrypted_filename, "rb") as file:
                    data = file.read(4096)
                    while data:
                        self.s.send(data)
                        data = file.read(4096)
                print("Sent Successfully")

if __name__ == "__main__":

    client = Client()
    # To Connect Client with Server
    client.connect_server()

    # Disconnect Server
    client.disconnect_server()