class InputValues:
    def __init__(self, render):
        self.render = render

    def _check_value(self, value):
        if str(value)[0] == '-':
            if all(str(v).isdigit() for v in value[1:]):
                return int(value)
                # all(str(v).isdigit() for v in value):

        if all(str(v).isdigit() for v in value):
            return int(value)

        return None

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [self._check_value(v) for v in func(*args, **kwargs).split()]

        return wrapper


class RenderDigit:
    def __call__(self, value):
        if str(value)[0] == '-':
            if all(str(v).isdigit() for v in value[1:]):
                return int(value)
                # all(str(v).isdigit() for v in value):

        if all(str(v).isdigit() for v in value):
            return int(value)

        return str(value)


@InputValues(render=RenderDigit())
def input_dg():
    return input()


res = input_dg()
print(res)
