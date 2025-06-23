import socket

SERVER_IP = "127.0.0.1"  # Replace with LAN IP of server
SERVER_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Type messages to send. Type 'exit' to quit.")
while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break
    sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
