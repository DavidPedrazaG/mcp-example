import socket
from shared.protocol import send_json, recv_json

def start_file_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 7002))
        s.listen()
        print("[FileServer] Esperando tareas en puerto 7002")
        while True:
            conn, addr = s.accept()
            with conn:
                task = recv_json(conn)
                print(f"[FileServer] Tarea recibida: {task}")
                action = task.get('action')
                params = task.get('params', {})

                if action == 'read':
                    filepath = params.get('path', '')
                    response = {"status": "ok", "file": filepath, "content": "Contenido simulado..."}
                else:
                    response = {"error": "acción desconocida"}

                send_json(conn, response)

if __name__ == "__main__":
    start_file_server()