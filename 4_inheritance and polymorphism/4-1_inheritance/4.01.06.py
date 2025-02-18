class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        pass

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def __init__(self, methods=('GET',)):
        super().__init__(methods)

    def get(self, request):
        if type(request) == dict:
            if request.keys() == {'url'}:
                return f"url: {request['url']}"
            else:
                raise TypeError('request не содержит обязательного ключа url')
        else:
            raise TypeError('request не является словарем')


    def render_request(self, request, method):
        if str(method).upper() not in self.methods:
            raise TypeError('данный запрос не может быть выполнен')
        else:
            return self.__getattribute__(method.lower())(request)


dv = DetailView()
html = dv.render_request({'url': 'https://site.ru/home'}, 'GET')  # url: https://site.ru/home
print(html)