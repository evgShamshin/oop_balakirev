class CPU:
    # CPU - класс для описания процессоров
    def __init__(self, name, fr):
        # name - наименование; fr - тактовая частота
        self.name = name
        self.fr = fr


class Memory:
    # Memory - класс для описания памяти
    def __init__(self, name, volume):
        # name - наименование; volume - объем памяти
        self.name = name
        self.volume = volume


class MotherBoard:
    # MotherBoard - класс для описания материнских плат
    def __init__(self, name, cpu, total_mem_slots, mem_slots):
        # name - наименование; cpu - ссылка на объект класса CPU; total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется); mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти)
        self.name = name
        self.cpu = CPU
        self.total_mem_slots = total_mem_slots
        self.mem_slots = Memory.__dict__.items()


    def get_config(self):
        config = [f'Материнская плата: {self.name}',
                  f'Центральный процессор: {CPU.__dict__['name']}, {CPU.__dict__['fr']} ',
                  f'Слотов памяти: {Memory.__dict__["total_mem_slots"]}',
                  'Память: <наименование_1> - <объем_1>; <наименование_2> - <объем_2>; ...; <наименование_N> - <объем_N>']
        return config


mb = MotherBoard()