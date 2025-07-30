import json
import socket

def send_json(sock: socket.socket, data: dict):
    message = json.dumps(data).encode()
    sock.sendall(message)

def recv_json(sock: socket.socket) -> dict:
    data = sock.recv(4096)
    return json.loads(data.decode())