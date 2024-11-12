from sys import stdin as s


class ListObject:
    def __init__(self, data, next_obj=None):
        self.data = data
        self.next_obj = next_obj

    def link(self, obj):
        self.next_obj = obj[:]


lst_in = list(map(str.strip, s.readlines()))

head_obj = ListObject(lst_in[0], lst_in[1])
