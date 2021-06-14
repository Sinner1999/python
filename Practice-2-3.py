import abc

class IShape(abc.ABC):
    '''Интерфейс для реализации геометрических фигур'''
    
    @abc.abstractmethod
    def get_perimeter(self):
        '''Возвращает периметр фигуры'''
        pass

    @abc.abstractmethod
    def get_area(self):
        '''Возвращает площадь фигуры'''
        pass

    @abc.abstractmethod
    def get_description(self):
        '''Возвращает произвольное описание фигуры'''
        pass

class Circle(IShape):
    def __init__(self, rad):
        self.__rad = rad
    
    def get_perimeter(self):
        return 2 * 3.14 * self.__rad

    def get_area(self):
        return 3.14 * self.__rad ** 2

    def get_description(self):
        return f'Я  - круг с радиусом {self.__rad}.'


class Rectangle(IShape):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    
    def get_perimeter(self):
        return (2 * self.__a) + (2 * self.__b)

    def get_area(self):
        return self.__a * self.__b

    def get_description(self):
        return f'Я  - прямоугольник со сторонами {self.__a} и {self.__b}.'

class Square(IShape):
    def __init__(self, a):
        self.__a = a
    
    def get_perimeter(self):
        return 4 * self.__a

    def get_area(self):
        return self.__rad ** 2

    def get_description(self):
        return f'Я  - квадрат со стороной {self.__a}.'

class Game:
    import random

    def get_shape(self):
        pass

    def calculate(self):
        pass

    def run(self):
        pass

    def play(self):
        self.run()


    # random.randrange(len(slovo) + 1)