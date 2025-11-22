import socket
import ssl

HOST = "0.0.0.0"
PORT = 5000

CERT_FILE = "server.crt"   
KEY_FILE = "server.key"    

# TLS-Kontext für den Server
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
 
    # Socket in TLS-Socket „einwickeln“
    with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        with conn:
            data = conn.recv(1024)
            print("Received:", data.decode("utf-8"))
