import socket
from shared.protocol import send_json, recv_json

def start_monitor_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 7001))
        s.listen()
        print("[MonitorServer] Esperando tareas en puerto 7001")
        while True:
            conn, addr = s.accept()
            with conn:
                task = recv_json(conn)
                print(f"[MonitorServer] Tarea recibida: {task}")
                action = task.get('action')
                if action == 'get_metrics':
                    response = {
                        "cpu": "15%",
                        "mem": "1.2GB"
                    }
                else:
                    response = {"error": "acción desconocida"}
                send_json(conn, response)

if __name__ == "__main__":
    start_monitor_server()