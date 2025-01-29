from sys import stdin as s


class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj
        return self

lst_in = list(map(str.strip, s.readlines()))

head_obj = ListObject(lst_in[0], lst_in[1])
lst_obj = [ListObject(lst_in[n], lst_in[n + 1]) for n, i in enumerate(lst_in[:-1])]
lst_obj.append(ListObject(lst_in[-1]))
lst_obj[0] = head_obj
res = [lst_obj[n].link(lst_obj[n + 1]).__dict__ for n, i in enumerate(lst_obj[:-1])]
