import abc
import random

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
        return round(2 * 3.14 * self.__rad, 2)

    def get_area(self):
        return round(3.14 * self.__rad ** 2, 2)

    def get_description(self):
        return f'Я  - круг с радиусом {self.__rad}.'


class Rectangle(IShape):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b
    
    def get_perimeter(self):
        return round((2 * self.__a) + (2 * self.__b), 2)

    def get_a(self):
        return self.__a
    width = property(get_a)

    def get_area(self):
        return round(self.__a * self.__b, 2)

    def get_description(self):
        return f'Я  - прямоугольник со сторонами {self.__a} и {self.__b}.'

class Square(Rectangle):
    def __init__(self, a):
        super().__init__(a, a)
    
    def get_description(self):
        return f'Я  - квадрат со стороной {super().width}.'

class Game:
    
    @staticmethod
    def __get_shape(fig):
        if fig == 0:
            f = Circle(random.randint(1, 50))
        elif fig == 1:
            f = Rectangle(random.randint(1, 50), random.randint(1, 50))
        elif fig == 2:
            f = Square(random.randint(1, 50))
        return f

    @staticmethod
    def __calculate(fig):
        print(fig.get_description())
        s = input('Укажите мою площадь: ')
        if s == str(fig.get_area()):
            print('Угадал!')
        else:
            print(f'Не угадал! Площадь равна {fig.get_area()}')
        p = input('Укажите мой периметр: ')
        if p == str(fig.get_perimeter()):
            print('Угадал!')
        else:
            print(f'Не угадал! Периметр равен {fig.get_perimeter()}')

    @classmethod
    def __run(cls):
        f = random.randrange(3)
        cls.__calculate(cls.__get_shape(f))


    @classmethod
    def play(cls):
        print('Привет! Мы геометрические фигуры и у нас есть 2 вопроса.')
        while input('Поиграем ?  Y/N:').upper() == 'Y':
            cls.__run()
        else:
            print('Спасибо за участие!!!')

Game.play()