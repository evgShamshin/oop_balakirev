# здесь объявляются все необходимые классы
class Graph:
    def __init__(self, data, is_show=True):
        self.data = data.copy()
        self.is_show = is_show

    def set_data(self, data):
        # для передачи нового списка данных в текущий график
        self.data = data.copy()

    def show_table(self):
        # для отображения данных в виде строки из списка чисел (числа следуют через пробел)
        if self.is_show is False:
            print("Отображение данных закрыто")
        else:
            print(*self.data)

    def show_graph(self):
        # для отображения данных в виде графика (метод выводит в консоль сообщение: "Графическое отображение данных: <строка из чисел следующих через пробел>")
        if self.is_show is False:
            print("Отображение данных закрыто")
        else:
            print("Графическое отображение данных:", end=" ")
            print(*self.data)

    def show_bar(self):
        # для отображения данных в виде столбчатой диаграммы (метод выводит в консоль сообщение: "Столбчатая диаграмма: <строка из чисел следующих через пробел>")
        if self.is_show is False:
            print("Отображение данных закрыто")
        else:
            print("Столбчатая диаграмма:", end=" ")
            print(*self.data)

    def set_show(self, fl_show):
        # метод для изменения локального свойства is_show на переданное значение fl_show. Если локальное свойство is_show равно False, то методы show_table(), show_graph() и show_bar() должны выводить сообщение: "Отображение данных закрыто"
        self.is_show = fl_show


# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()