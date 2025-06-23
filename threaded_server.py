import socket
import threading
from packet import Packet
from arp import ARPTable

# Server configuration
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

# Initialize ARP and socket
arp_table = ARPTable()
server_mac = arp_table.fake_mac(SERVER_IP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((SERVER_IP, SERVER_PORT))

# Track connected clients
clients = set()

# Thread to receive messages
def receive_messages():
    while True:
        try:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            packet = Packet.from_bytes(data)
            clients.add(addr)
            print(f"\n--- Received ARP + Encapsulation ---\n{packet.encapsulate()}")
            print(f"\n[Received Packet]:\n{packet}")
            print("Reply: ", end='')
        except Exception as e:
            print(f"[Error in receive]: {e}")

# Thread to send replies
def send_messages():
    while True:
        reply = input("Reply: ")
        for client in clients:
            dest_ip = client[0]
            dest_port = client[1]
            dest_mac = arp_table.resolve(dest_ip)
            response_packet = Packet(SERVER_IP, dest_ip, SERVER_PORT, dest_port, reply,
                                     src_mac=server_mac, dest_mac=dest_mac)
            print(f"\n--- ARP & Encapsulation for Reply ---\n{response_packet.encapsulate()}")
            print(f"\n[Sending Packet]:\n{response_packet}\n")
            sock.sendto(response_packet.to_bytes(), client)

# Start server
print(f"[Server] Listening on {SERVER_IP}:{SERVER_PORT}")

# Start receiving in a background thread
recv_thread = threading.Thread(target=receive_messages, daemon=True)
recv_thread.start()

# Run the send loop
send_messages()

