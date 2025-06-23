# 🧠 LAN Communication Suite (Python-based Network Simulation)

A protocol simulation project built in Python to emulate how real network communication works over LAN using the OSI model. This system demonstrates client-server messaging using **UDP sockets**, enhanced with **custom packet encapsulation**, **ARP simulation**, and **multi-layer protocol visibility**.

---

## 📌 Project Goals

- Simulate real-world LAN communication aligned with the OSI model
- Understand Transport (UDP), Network (IP), and Data Link (MAC) layers
- Log every encapsulation step (like a CLI-based Wireshark)
- Introduce protocol simulation including ARP and error handling

---

## 🏗️ Current Progress (Days 1–5)

### ✅ Day 1: Basic UDP Client-Server Chat
- Created a simple UDP server and client
- Single-direction messaging over `127.0.0.1` or LAN IP

### ✅ Day 2: Multithreaded Two-Way Chat
- Enabled full-duplex communication using Python `threading`
- Clients and server can send/receive concurrently

### ✅ Day 3: Simulated Packet Class
- Introduced a custom `Packet` class to wrap messages
- Simulated Transport and Network headers (IP + Port)
- Serialized data using JSON before sending

### ✅ Day 4: OSI Layer Encapsulation Logs
- Simulated Application → Transport → Network → Data Link headers
- Printed each layer’s encapsulation log before transmission

### ✅ Day 5: ARP Table Simulation
- Simulated Address Resolution Protocol (ARP) manually
- Mapped IPs to fake MACs before packet transmission
- Logged ARP requests and replies just like in real LAN

---

## 🧰 Technologies Used

| Tool/Concept       | Usage                                  |
|--------------------|-----------------------------------------|
| `Python`           | Core language for simulation            |
| `socket`           | UDP communication                      |
| `threading`        | Enable full-duplex real-time chat       |
| `json`             | Packet serialization                   |
| `custom ARP`       | IP → MAC mapping simulation             |

---

## 🗂️ Project Structure

