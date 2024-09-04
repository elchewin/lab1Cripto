import sys
import time
import random
from scapy.all import IP, ICMP, send

def crear_paquete_icmp(destino, secuencia, caracter):
    """
    Crear un paquete ICMP con un carácter específico en el campo de datos.
    """
    # Construcción del paquete ICMP
    paquete = IP(dst=destino) / ICMP(type=8, code=0, id=3, seq=secuencia) / caracter
    return paquete

def main():
    # Verificación de argumentos
    if len(sys.argv) < 2:
        print("Uso: sudo python3 pingv4.py \"<texto_a_enviar>\"")
        sys.exit(1)

    # Texto a enviar
    texto = sys.argv[1]

    # Dirección de destino (por ejemplo, una IP local o de prueba)
    destino = "192.168.177.49"

    # Crear y enviar paquetes ICMP para cada carácter en el texto
    for indice, caracter in enumerate(texto):
        paquete = crear_paquete_icmp(destino, secuencia=indice+1, caracter=caracter)
        send(paquete, verbose=False)
        print(".")
        time.sleep(0.5)  # Esperar medio segundo entre paquetes para simular un tráfico normal

if __name__ == "__main__":
    main()