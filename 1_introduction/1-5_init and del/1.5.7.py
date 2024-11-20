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
    def __init__(self, name, cpu, *mem_slots):
        # name - наименование;
        # cpu - ссылка на объект класса CPU;
        # total_mem_slots = 4 - общее число слотов памяти (атрибут прописывается с этим значением и не меняется);
        # mem_slots - список из объектов класса Memory (максимум total_mem_slots = 4 штук по максимальному числу слотов памяти)
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots]

    def get_config(self):
        config = [f"Материнская плата: {self.name}",
                  f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
                  f"Слотов памяти: {self.total_mem_slots}",
                  f"Память: {'; '.join([f'{i.name} - {i.volume}' for i in self.mem_slots])}"]
        return config


# Пример создания объектов и получения конфигурации
cpu = CPU("Intel Core i7", "3.6GHz")
mem1 = Memory("Corsair", "16GB")
mem2 = Memory("Kingston", "8GB")
mb = MotherBoard("ASUS ROG", cpu, mem1, mem2)

# Получение конфигурации (ничего не отображаем на экране, как указано)
config = mb.get_config()