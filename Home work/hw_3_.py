class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu  # Приватный атрибут
        self.__memory = memory  # Приватный атрибут

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        # Пример арифметических вычислений
        return self.__cpu * self.__memory

    def __str__(self):
        return f"Computer with CPU: {self.__cpu}, Memory: {self.__memory}"

    # Магические методы сравнения
    def __eq__(self, other):
        return self.memory == other.memory

    def __ne__(self, other):
        return self.memory != other.memory

    def __lt__(self, other):
        return self.memory < other.memory

    def __le__(self, other):
        return self.memory <= other.memory

    def __gt__(self, other):
        return self.memory > other.memory

    def __ge__(self, other):
        return self.memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list  # Приватный атрибут

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        if 0 < sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}.")
        else:
            print("Неверный номер сим-карты.")

    def __str__(self):
        return f"Phone with SIM cards: {', '.join(self.__sim_cards_list)}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Построение маршрута до {location}.")

    def __str__(self):
        return f"SmartPhone with CPU: {self.cpu}, Memory: {self.memory}, SIM cards: {', '.join(self.sim_cards_list)}"


# Создание объектов
computer = Computer(cpu=4.0, memory=16)
phone = Phone(sim_cards_list=["Beeline", "MegaCom"])
smartphone1 = SmartPhone(cpu=2.5, memory=8, sim_cards_list=["Beeline", "O!", "MegaCom"])
smartphone2 = SmartPhone(cpu=3.0, memory=12, sim_cards_list=["Beeline"])

# Распечатка информации об объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Опробуем методы объектов
print("Computations:", computer.make_computations())
phone.call(1, "+996 777 99 88 11")
smartphone1.use_gps("Бишкек")
smartphone2.call(2, "+996 555 44 33 22")

# Тестирование магических методов сравнения
print("Сравнение памяти компьютера и смартфонов:")
print(computer < smartphone1)
print(computer > smartphone2)
print(smartphone1 == smartphone2)