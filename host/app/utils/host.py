import json
from clients.monitor_client import MonitorClient
from clients.file_client import FileManagerClient
from clients.db_client import DatabaseClient
from app.schemas.prompt import PromptRequest, PromptResponse    

class MCPHost:
    def __init__(self, task_file='tasks.json', request: PromptRequest = None):
        self.clients = {
            'monitor': MonitorClient() if request and request.monitor else None,
            'file': FileManagerClient() if request and request.file else None,
            'db': DatabaseClient() if request and request.db else None
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
