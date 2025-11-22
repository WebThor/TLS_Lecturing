import socket

HOST = "127.0.0.1"
PORT = 5000

with socket.create_connection((HOST, PORT)) as s:
    s.sendall(b"username=alice&password=SuperSecret123")