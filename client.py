import socket


HEADER = 4
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# Make a string type variable call it SERVER and use your ipv4 address for client 
SERVER = '127.0.1.1'
ADDR = (SERVER, PORT) 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Ola!")
send("ras shobi")
send("kargad")
send("naxvamdis")

send(DISCONNECT_MESSAGE)
