import json
from clients.monitor_client import MonitorClient
from clients.file_client import FileManagerClient
from clients.db_client import DatabaseClient

class MCPHost:
    def __init__(self, task_file='tasks.json'):
        self.clients = {
            'monitor': MonitorClient(),
            'file': FileManagerClient(),
            'db': DatabaseClient()
        }
        with open(task_file) as f:
            self.tasks = json.load(f)

    def run(self):
        print("[HOST] Ejecutando tareas desde tasks.json\n")
        for task in self.tasks:
            task_type = task.get('type')
            client = self.clients.get(task_type)
            if client:
                client.send_task(task)
            else:
                print(f"[HOST] Cliente desconocido para tipo: {task_type}")

if __name__ == "__main__":
    host = MCPHost()
    host.run()