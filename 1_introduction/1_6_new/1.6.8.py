TYPE_OS = 1 # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"


class Dialog:
    """"
     dlg = Dialog(<название>)
     Здесь <название> - это строка, которая сохраняется в локальном свойстве name объекта dlg.
     """
    __instance = None

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            cls.__instance = DialogWindows()
        if TYPE_OS == 2:
            cls.__instance = DialogLinux()
        setattr(cls.__instance, "name", args[0])
        return cls.__instance