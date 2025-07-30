import socket
from shared.protocol import send_json, recv_json

class MCPClientBase:
    def __init__(self, name, port):
        self.name = name
        self.port = port

    def send_task(self, task: dict) -> dict:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(('localhost', self.port))
            print(f"[{self.name}] Enviando tarea: {task}")
            send_json(s, task)
            response = recv_json(s)
            print(f"[{self.name}] Respuesta recibida: {response}")
            return response