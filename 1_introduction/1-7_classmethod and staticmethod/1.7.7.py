class TextInput:
    def __init__(self, name, size=10):
        """
        :param name: название для поля
        :param size: размер поля ввода
        """
        self.name = name
        self.size = size

    def get_html(self):
        """
        :return: возвращает сформированную HTML-строку в формате
        <p class='login'><имя поля>: <input type='text' size=<размер поля> />
        """
        pass

    @classmethod
    def check_name(cls, name):
        """
        :param name: имя для проверки
        - длина имени не менее 3 символов и не более 50;
        - в именах могут использоваться только символы русского, английского алфавитов, цифры и пробелы
        """
        from string import ascii_lowercase, digits

        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
        CHARS_CORRECT = CHARS + CHARS.upper() + digits
        if name in CHARS_CORRECT and 50 > len(name) > 3:
            return True
        raise ValueError("некорректное поле name")

    class PasswordInput:
        def __init__(self, name, size=10):
            """
            :param name: название для поля
            :param size: размер поля ввода
            """
            self.name = name
            self.size = size

    class FormLogin:
        def __init__(self, lgn, psw):
            self.login = lgn
            self.password = psw

        def render_template(self):
            return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])

    login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
    html = login.render_template()
