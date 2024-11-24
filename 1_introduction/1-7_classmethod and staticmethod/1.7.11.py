class Viber:
    list_msg = []

    @classmethod
    def add_message(cls, msg):
        cls.list_msg.append(msg)

    @classmethod
    def remove_message(cls, msg):
        cls.list_msg.remove(msg)

    @classmethod
    def set_like(cls, msg):
        like = cls.list_msg[cls.list_msg.index(msg)]
        if like.fl_like == False:
            like.fl_like = True
        else:
            like.fl_like = False

    @classmethod
    def show_last_message(cls, num):
        print(cls.list_msg[-num])

    @classmethod
    def total_messages(cls):
        return len(cls.list_msg)


class Message:
    def __init__(self, text, fl_like=False):
        self.text = text
        self.fl_like = fl_like


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
print(Viber.list_msg[Viber.list_msg.index(msg)].fl_like)
Viber.set_like(msg)
print(Viber.list_msg[Viber.list_msg.index(msg)].fl_like)
Viber.set_like(msg)
print(Viber.list_msg[Viber.list_msg.index(msg)].fl_like)