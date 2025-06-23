class ARPTable:
    def __init__(self):
        self.table = {}

    def resolve(self, ip):
        if ip in self.table:
            print(f"[ARP] Found in table: {ip} → {self.table[ip]}")
            return self.table[ip]
        else:
            # Simulate ARP request
            print(f"[ARP] Sending ARP request for {ip}")
            mac = self.fake_mac(ip)
            self.table[ip] = mac
            print(f"[ARP] Received ARP reply: {ip} → {mac}")
            return mac

    def fake_mac(self, ip):
        # Just make a MAC from the IP for simulation
        return "FA:KE:" + ":".join(ip.split("."))
