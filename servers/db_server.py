import socket
from shared.protocol import send_json, recv_json

def start_db_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 7003))
        s.listen()
        print("[DBServer] Esperando tareas en puerto 7003")
        while True:
            conn, addr = s.accept()
            with conn:
                task = recv_json(conn)
                print(f"[DBServer] Tarea recibida: {task}")
                action = task.get('action')
                if action == 'insert':
                    response = {"status": "ok", "message": "Registro insertado"}
                else:
                    response = {"error": "acción desconocida"}
                send_json(conn, response)

if __name__ == "__main__":
    start_db_server()