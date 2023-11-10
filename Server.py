import os
import socket
from _thread import *
import sys

from dotenv import load_dotenv

load_dotenv()
SERVER = os.getenv('IPV4')
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
