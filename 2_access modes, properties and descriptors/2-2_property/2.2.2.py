class Test:
    def __init__(self):
        self.__test = 0

    def set_test(self, value):
        self.__test = value

    def get_test(self):
        return self.__test

    def del_test(self):
        del self.__test

    """ #1
    pr = property()
    pr = pr.setter(set_test)
    pr = pr.getter(get_test)
    pr = pr.deleter(del_test)
    """

    # pr = property(get_test, set_test, del_test) #2

    # pr = property(get_test) #3



t = Test()
print(t.pr)
