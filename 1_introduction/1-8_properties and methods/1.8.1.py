class Server:
    def send_data(data):
        pass

    def get_data(self):
        pass

    def get_ip(self):
        pass


class Router:
    buffer = {}
    def link(self, server):
        setattr(self, "server", server)

    def unlink(self, server):
        delattr(self, server)

    def send_data(self, data, ip):
        self.buffer.setdefault(ip, data)
        print(self.buffer)
        self.buffer = {}
        print(self.buffer)

class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip


router = Router()
sv_from = Server()
router.send_data("data", "ip")