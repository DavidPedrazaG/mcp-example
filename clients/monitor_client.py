from clients.base import MCPClientBase

class MonitorClient(MCPClientBase):
    def __init__(self):
        super().__init__('MonitorClient', 7001)
