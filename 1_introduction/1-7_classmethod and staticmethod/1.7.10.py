class AppStore:
    store = []

    def add_application(self, app):
        self.store.append(app)

    def remove_application(self, app):
        self.store.remove(app)

    def block_application(self, app):
        self.store[self.store.index(app)].blocked = True

    def total_apps(self):
        return len(self.store)


class Application:
    def __init__(self, name, blocked=False):
        self.name = name
        self.blocked = blocked

store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
print(store.block_application(app_youtube))