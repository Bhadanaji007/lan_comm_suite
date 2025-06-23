import socket
import threading
from packet import Packet
from arp import ARPTable

CLIENT_IP = socket.gethostbyname(socket.gethostname())
CLIENT_PORT = 12345
SERVER_IP = "127.0.0.1"
SERVER_PORT = 5005
BUFFER_SIZE = 1024

arp_table = ARPTable()
client_mac = arp_table.fake_mac(CLIENT_IP)
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((CLIENT_IP, CLIENT_PORT))

def receive_messages():
    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        packet = Packet.from_bytes(data)
        print(f"\n[From Server]:\n{packet}\nYou: ", end='')

recv_thread = threading.Thread(target=receive_messages, daemon=True)
recv_thread.start()

print("Type messages to send. Type 'exit' to quit.")
while True:
    message = input("You: ")
    if message.lower() == 'exit':
        break

    dest_mac = arp_table.resolve(SERVER_IP)
    packet = Packet(CLIENT_IP, SERVER_IP, CLIENT_PORT, SERVER_PORT, message,
                    src_mac=client_mac, dest_mac=dest_mac)
    print(f"\n--- ARP & Encapsulation ---\n{packet.encapsulate()}")
    print(f"\n[Sending Packet]:\n{packet}\n")
    sock.sendto(packet.to_bytes(), (SERVER_IP, SERVER_PORT))

sock.close()


