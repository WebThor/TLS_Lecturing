import socket
import ssl

HOST = "127.0.0.1"   # oder "localhost"
PORT = 5000

# TLS-Client-Kontext mit Zertifikatsprüfung
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations("server.crt")   # Server-Zertifikat als vertrauenswürdig laden

SERVER_NAME = "localhost"  # muss zum CN/SAN im Zertifikat passen

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=SERVER_NAME) as tls_sock:
        tls_sock.sendall(b"username=alice&password=SuperSecret123")