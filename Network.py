import os
import socket

from dotenv import load_dotenv

load_dotenv()
SERVER = os.getenv('IPV4')
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = SERVER
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connected()
        print(self.id)

    def connected(self):
        try:
            self.client.connected(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
