import json

class Packet:
    def __init__(self, src_ip, dest_ip, src_port, dest_port, payload,
                 src_mac="00:00:00:00:00", dest_mac="00:00:00:00:00"):
        self.src_ip = src_ip
        self.dest_ip = dest_ip
        self.src_port = src_port
        self.dest_port = dest_port
        self.payload = payload
        self.src_mac = src_mac
        self.dest_mac = dest_mac

    def encapsulate(self):
        log = []
        log.append(f"[Application Layer] Payload: {self.payload}")
        log.append(f"[Transport Layer] Src Port: {self.src_port}, Dest Port: {self.dest_port}")
        log.append(f"[Network Layer] Src IP: {self.src_ip}, Dest IP: {self.dest_ip}")
        log.append(f"[Data Link Layer] Src MAC: {self.src_mac}, Dest MAC: {self.dest_mac}")
        return "\n".join(log)

    def to_bytes(self):
        return json.dumps(self.__dict__).encode()

    @staticmethod
    def from_bytes(data_bytes):
        data = json.loads(data_bytes.decode())
        return Packet(**data)

    def __str__(self):
        return (
            f"[PACKET STRUCTURE]\n"
            f"Src: {self.src_ip}:{self.src_port} → Dest: {self.dest_ip}:{self.dest_port}\n"
            f"Src MAC: {self.src_mac} → Dest MAC: {self.dest_mac}\n"
            f"Payload: {self.payload}"
        )

