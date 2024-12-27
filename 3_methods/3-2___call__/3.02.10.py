class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        # def wrapper(num):
        pass


class RenderDigit:
    def __call__(self, value):
        if str(value)[0] == '-':
            if all(str(v).isdigit() for v in value[1:]):
                return True
                # all(str(v).isdigit() for v in value):

        if all(str(v).isdigit() for v in value):
            return True

        return False


render = RenderDigit()
r1 = render("a12")
print(r1)
