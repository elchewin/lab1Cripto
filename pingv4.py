from scapy.all import *
import time
import random
import struct
from datetime import datetime

def create_icmp_packet(character, sequence_number):
    # Crear una cabecera IP
    ip = IP()
    ip.src = "64.233.186.102"  # Dirección IP de origen simulada
    ip.dst = "192.168.177.49"  # Dirección IP de destino simulada
    ip.ttl = 99  # Time to Live

    # Crear una cabecera ICMP con un solo carácter como datos
    icmp = ICMP()
    icmp.type = 8  # Echo Request
    icmp.code = 0
    icmp.seq = sequence_number
    icmp.id = random.randint(0, 65535)  # Identificador aleatorio

    # Obtener el timestamp actual en GMT-4 y convertirlo en formato de timestamp hexadecimal
    current_time = datetime.utcnow().timestamp() - (4 * 3600)
    timestamp_hex = struct.pack("<Q", int(current_time))
    timestamp_hex = timestamp_hex[::-1]  # Revertir el orden para simular Wireshark

    # Establecer los datos del paquete con el carácter y el timestamp
    icmp_payload = bytes(character, 'utf-8') + timestamp_hex
    icmp.add_payload(icmp_payload)

    # Construir el paquete completo
    packet = ip / icmp
    return packet

def send_icmp_packets(text):
    sequence_number = 0  # Inicializa el número de secuencia

    for character in text:
        packet = create_icmp_packet(character, sequence_number)
        send(packet, verbose=0)  # Enviar el paquete ICMP sin mostrar salida detallada
        print(".\nSent 1 packets.")
        time.sleep(1)  # Pausar 1 segundo entre paquetes para simular tráfico real
        sequence_number += 1  # Incrementar el número de secuencia

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Uso: sudo python3 pingv4.py \"<texto>\"")
        sys.exit(1)

    text_to_send = sys.argv[1]
    send_icmp_packets(text_to_send)