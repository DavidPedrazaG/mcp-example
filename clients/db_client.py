from clients.base import MCPClientBase

class DatabaseClient(MCPClientBase):
    def __init__(self):
        super().__init__('DatabaseClient', 7003)