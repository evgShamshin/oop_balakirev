# здесь объявляйте классы
class StringException(Exception):...


class NegativeLengthString(StringException):...


class ExceedLengthString(StringException):...


class PrintData:
    def __init__(self):
        raise ExceedLengthString


try:
    PrintData()
except NegativeLengthString:
    print("NegativeLengthString")
except ExceedLengthString:
    print("ExceedLengthString")
except StringException:
    print("StringException")
