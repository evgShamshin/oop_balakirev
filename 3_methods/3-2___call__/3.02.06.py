class RenderList:
    def __init__(self, type_list='ul'):
        if type_list == 'ol':
            self.type_list = type_list
        else:
            self.type_list = 'ul'

    def __call__(self, lst):
        sep = self.type_list
        return ((f'<{sep}>\n' +
                 ''.join('<li>' + l + '</li>\n' for l in lst)) +
                f'</{sep}>\n')


l = ['123']
render = RenderList()
print(render(l))
