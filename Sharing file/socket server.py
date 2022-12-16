import socket
import os
from cryptography.fernet import Fernet

class Server:

    def __init__(self):
        # Create a socket object
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   
    def start_server(self):
        # Create a socket object
        # IP and port of the machine where server is running
        host = '127.0.0.1'
        port = 5000
        
        # Bind and Listen to the Port
        self.s.bind((host, port))
        self.s.listen()
        c, addr = self.s.accept()
        print ("Got connection from", str(addr))


    def receive_data(self, c, addr):
        # key generation
        key = Fernet.generate_key()

        # opening the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()

        # using the key
        fernet = Fernet(key)

        # opening the encrypted file
        with open('output2.txt', 'rb') as enc_file:
            encrypted = enc_file.read()

        # decrypting the file
        decrypted = fernet.decrypt(encrypted)

        # opening the file in write mode and
        # writing the decrypted data
        with open('output3.txt', 'wb') as dec_file:
            dec_file.write(decrypted)

        c.close()

if __name__ == "__main__":
    server = Server()
    server.start_server()
