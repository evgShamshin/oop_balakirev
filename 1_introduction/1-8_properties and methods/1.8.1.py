class Server:
    buffer = []
    counter = 0

    def __new__(cls, *args, **kwargs):
        cls.counter = + 1
        return cls.counter

    def __init__(self, *args, **kwargs):
        self.counter =+ 1
        self.ip = self.counter

    def send_data(self, data):
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


# router = Router()
sv_from1 = Server()
# router.send_data("data", "ip")
print(sv_from1)
# sv_from2 = Server()
# print(sv_from2)
