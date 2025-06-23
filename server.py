import socket

SERVER_IP = "127.0.0.1"  # Replace with LAN IP if needed
SERVER_PORT = 5005
BUFFER_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

print(f"[Server] Listening on {SERVER_IP}:{SERVER_PORT}")

while True:
    data, addr = sock.recvfrom(BUFFER_SIZE)
    print(f"[Received from {addr}]: {data.decode()}")
