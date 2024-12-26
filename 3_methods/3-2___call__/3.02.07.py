class HandlerGET:
    def __init__(self, func):
        self.func = func

    def __call__(self, request):
        if ('method' in request and request['method'] == 'GET')\
                or 'method' not in request:
            return self.get(self.func, request)
        else:
            return None

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'


@HandlerGET
def index(request):
    return "главная страница сайта"


res = index({"method": "GET"})
print(res)
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert res == "GET: главная страница сайта", "декорированная функция вернула неверные данные"