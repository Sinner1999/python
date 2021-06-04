class Point:
    def __init__(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def __repr__(self):
        return f'Point - x = "{self.__x}", y = "{self.__y}".'

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
         self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
         self.__y = value

    def move_to(self, x = 0, y = 0):
        self.__x = x
        self.__y = y

    def move_by(self, x = 0, y = 0):
        self.__x += x
        self.__y += y


    
a = Point(10,20)
print(a)
a.move_to(100,200)
print(a)
a.move_by(10,20)
print(a)
a.x = 30
a.y = 40
print(a)