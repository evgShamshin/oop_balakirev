class FileAcceptor:
    def __init__(self, *args):
        self.ext = args

    @staticmethod
    def check_contain(data, ext):
        for e in ext:
            if e in data:
                return True
        return False

    def __call__(self, *args):
        return [a.split() for a in args[0] if self.check_contain(a, self.ext)]

    def __add__(self, other):
        res = list(self.ext)
        for oth in other.ext:
            if oth not in res:
                res.append(oth)
        return res


filenames_list = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls", "eq_3,png", "text1.sxls", "doc", "doc.docx", "doc."]

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames_list))
print(filenames)
assert filenames == ['boat.jpg', 'ans.web.png', 'text.txt', 'www.python.doc', 'my.ava.jpg', 'forest.jpeg', 'eq_1.png', 'eq_2.xls']