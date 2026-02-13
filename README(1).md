# DHCP Spoofing Attack  
## Technical Documentation

---

## Legal Notice

This project has been developed **strictly for educational purposes and authorized security auditing**.  
Any use of this tool against networks, systems, or infrastructures **without explicit authorization** is illegal and may result in legal consequences.

The author assumes **no responsibility** for misuse of the information or code provided.

---

## 1. Overview

DHCP Spoofing is a network-based attack in which an adversary deploys a **rogue DHCP server** within a Local Area Network (LAN) in order to distribute malicious network configuration parameters to legitimate clients.

By responding faster than the legitimate DHCP server, the attacker can assign:
- A malicious default gateway
- A controlled DNS server
- Arbitrary IP addressing

This attack is commonly used as a preliminary step for more advanced threats such as:
- Man-in-the-Middle (MitM) attacks
- Traffic interception and analysis
- Credential harvesting
- Denial of Service (DoS)

---

## 2. Objective of the Script

The objective of this script is to **demonstrate and analyze the DHCP Spoofing attack in a controlled laboratory environment**, allowing students and security professionals to:

- Understand the internal operation of the DHCP protocol
- Identify vulnerabilities in networks without access controls
- Evaluate the impact of rogue DHCP servers
- Apply appropriate defensive countermeasures

---

## 3. Network Topology

| Device | Description | IP Address |
|------|-------------|------------|
| Legitimate Router | Authorized network gateway | 192.168.1.1 |
| Victim Host | DHCP client | Assigned dynamically |
| Attacker Machine | Kali Linux rogue DHCP | 192.168.1.200 |
| Switch | Layer 2 device | VLAN 1 |

---

## 4. Parameters Used

- Network interface: eth0
- Rogue default gateway: 192.168.1.200
- Malicious DNS server: Controlled by attacker
- DHCP scope: Faster response than legitimate server

---

## 5. Requirements

- Linux OS (Kali Linux recommended)
- Python 3.x
- Scapy library
- Root or sudo privileges

```bash
sudo apt update
sudo apt install python3-scapy -y
```

---

## 6. Evidence and Screenshots

All screenshots must be stored in:

```
/images
```

---

## 7. Mitigation Strategies

- Enable DHCP Snooping
- Configure trusted/untrusted ports
- VLAN segmentation
- DHCP traffic monitoring
- Implement 802.1X

```bash
ip dhcp snooping
ip dhcp snooping vlan 1
```

---

## 8. Ethical Use Policy

This tool must be used **only** for academic labs and authorized security testing.  
Unauthorized usage is strictly prohibited.

---

## 9. Author

**Max (Reily Castillo Del Rosario)**  
Cybersecurity Student  
Dominican Republic  

---

## 10. Contributions

Contributions are welcome for educational improvements only.  
Fork the repository and submit a Pull Request with documentation.

---

## 11. License

This project is licensed under the **MIT License**.
