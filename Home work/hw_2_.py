class Figure:
    unit = 'cm'  # Уровень класса: единица измерения

    def __init__(self):
        pass

    def calculate_area(self):
        raise NotImplementedError("This method should be overridden in derived classes.")

    def info(self):
        raise NotImplementedError("This method should be overridden in derived classes.")


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length  # Приватный атрибут

    def calculate_area(self):
        return self.__side_length ** 2  # Площадь квадрата

    def info(self):
        area = self.calculate_area()
        print(f"Square side length: {self.__side_length}{self.unit}, area: {area}{self.unit}.")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length  # Приватный атрибут
        self.__width = width    # Приватный атрибут

    def calculate_area(self):
        return self.__length * self.__width  # Площадь прямоугольника

    def info(self):
        area = self.calculate_area()
        print(f"Rectangle length: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}.")


# Исполняемая область
if __name__ == "__main__":
    # Создаем список фигур
    figures = [
        Square(5),
        Square(7),
        Rectangle(5, 8),
        Rectangle(3, 4),
        Rectangle(6, 2)
    ]

    # Вызываем метод info для всех фигур
    for figure in figures:
        figure.info()