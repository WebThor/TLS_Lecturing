import socket
import ssl

HOST = "127.0.0.1"
PORT = 5000

CERT_FILE = "server.crt"   
KEY_FILE = "server.key"    

# TLS-Kontext für den Server
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((HOST, PORT))
    conn, addr = sock.accept()
    with context.wrap_socket(conn, server_side=True) as tls_conn:
        data = tls_conn.recv(1024)
        print("Received:", data.decode("utf-8", errors="replace"))
