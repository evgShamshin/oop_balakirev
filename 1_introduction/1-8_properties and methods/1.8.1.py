class Server:
    count = 0
    router_obj = None

    def __init__(self):
        Server.count += 1
        self.ip = Server.count
        self.buffer = list()

    def send_data(self, data):
        self.router_obj.buffer.setdefault(data.ip, []).append(data)

    def get_data(self):
        setattr(self, "zalupa", self.buffer)
        self.buffer = []
        return self.zalupa


    def get_ip(self):
        return self.ip


class Router:
    list_server = []
    buffer = {}

    def link(self, server):
        self.list_server.append(server)
        server.router_obj = self

    def unlink(self, server):
        self.list_server.remove(server)
        server.router_obj = None

    def send_data(self):
        for i in self.buffer:
            for j in self.list_server:
                if i == j.ip:
                    j.buffer = self.buffer[i]
        self.buffer.clear()


class Data:
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip



router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from)
print(msg_lst_to)


"""
ZALUPA EBANAYA BLIAT, IDI NA HUY
data1 = Data('data1', 1)
data2 = Data('data2', 2)
data3 = Data('data3', 3)

router = Router()

sv_from1 = Server()
sv_from2 = Server()
sv_from3 = Server()

print(f"sv_from1 - {sv_from1}")
print(f"sv_from2 - {sv_from2}")
print(f"sv_from3 - {sv_from3}")
print()
print(f"sv_from1.__dict__ - {sv_from1.__dict__}")
print(f"sv_from2.__dict__ - {sv_from2.__dict__}")
print(f"sv_from3.__dict__ - {sv_from3.__dict__}")
print()

router.link(sv_from1)
router.link(sv_from2)
router.link(sv_from3)

print(f"router.list_server - {router.list_server}")
print(f"sv_from1.router_obj - {sv_from1.router_obj}")
print(f"sv_from2.router_obj - {sv_from2.router_obj}")
print(f"sv_from3.router_obj - {sv_from3.router_obj}")
print()

sv_from1.send_data(data1)
sv_from2.send_data(data2)

print(f"router.buffer - {router.buffer}")

router.send_data(data1, sv_from1.ip)"""