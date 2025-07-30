from clients.base import MCPClientBase

class FileManagerClient(MCPClientBase):
    def __init__(self):
        super().__init__('FileManagerClient', 7002)