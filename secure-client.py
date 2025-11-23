# secure_client_verified.py
import socket
import ssl
import time

HOST = "127.0.0.1"
PORT = 5000

# Kontext mit Zertifikats- und Hostname-Prüfung
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations("server.crt")  # self-signed Zertifikat als "CA" vertrauen

SERVER_NAME = "localhost"  # muss zum CN/SAN im Zertifikat passen

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=SERVER_NAME) as tls_sock:
        print("TLS established. Protocol:", tls_sock.version())
        tls_sock.sendall(b"username=alice&password=SuperSecret123\n")
        time.sleep(1)
