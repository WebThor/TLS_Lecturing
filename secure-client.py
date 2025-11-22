import socket
import ssl

HOST = "127.0.0.1"
PORT = 5000

context = ssl._create_unverified_context()  # keine Zertifikatsprüfung

with socket.create_connection((HOST, PORT)) as sock:
    with context.wrap_socket(sock, server_hostname=HOST) as tls_sock:
        tls_sock.sendall(b"username=alice&password=SuperSecret123")
