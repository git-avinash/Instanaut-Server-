import socket
import json

HEADERSIZE = 10
SERVER = socket.gethostname()
PORT = 5050
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDR)
msg = {
    'command': 'test',
    'username': 'avinash',
    'password': '123456',
}
msg = json.dumps(msg)
msg = f"{len(msg):<{HEADERSIZE}}" + msg
print(msg)
s.send(bytes(msg, FORMAT))
