class FileAcceptor:
    def __init__(self, *args):
        self.ext = args

    @staticmethod
    def check_contain(data, ext):
        if "." in data:
            data_in = data.split(".")

            for e in ext:
                if e == data_in[-1]:
                    return True
        return False

    def __call__(self, args):
        if type(args) in (list, tuple):
            return [a.split() for a in args[0] if self.check_contain(a, self.ext)]
        if type(args) == str:
            return self.check_contain(args, self.ext)

    def __add__(self, other):
        other_data = other.ext if isinstance(other, FileAcceptor) else [other]
        self_data = self.ext if isinstance(self, FileAcceptor) else [self]
        return FileAcceptor(*other_data + self_data)


filenames_list = ["boat.jpg", "ans.web.png", "text.txt", "www.python.doc", "my.ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.xls", "eq_3,png", "text1.sxls", "doc", "doc.docx", "doc."]

acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")
filenames = list(filter(acceptor_images + acceptor_docs, filenames_list))
print(filenames)
assert filenames == ['boat.jpg', 'ans.web.png', 'text.txt', 'www.python.doc', 'my.ava.jpg', 'forest.jpeg', 'eq_1.png', 'eq_2.xls']