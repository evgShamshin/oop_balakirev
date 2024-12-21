class ImageFileAcceptor:
    def __init__(self, extensions):
        self.__extensions = extensions

    def __call__(self, filename):
        return any([ext in filename.split(".") for ext in self.__extensions])



fs = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
acceptor = ImageFileAcceptor(("jpg", "png"))
res = filter(acceptor, fs)
assert set(res) == set(["boat.jpg", "web.png", "ava.8.jpg", "eq_1.png", "eq_2.png"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"

acceptor = ImageFileAcceptor(("jpeg", "html"))
res = filter(acceptor, fs)
print(list(res))
assert set(res) == set(["forest.jpeg", "my.html"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"
