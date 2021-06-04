class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point - x = "{self.x}", y = "{self.y}"'

    
    def move_to(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Point_3d(Point):
    def __init__(self, x = 0, y = 0, z = 0):
        self.z = z
        super().__init__(x, y)
        
    def move_by(self, x = 0, y = 0, z = 0):
        self.x += x
        self.y += y
        self.z += z
    
    def move_to(self, x = 0, y = 0, z = 0):
        self.z = z
        super().moove_to(x, y)
        
    def __repr__(self):
        s = super().__repr__()
        return f'{s}, z = "{self.z}"'
    
import random

class Human:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex.upper()
        self.status = None
        
    def __add__(self, human):
        if isinstance(human, Human):
            self.status = human
            human.status = self
        else:
            raise TypeError('Not a human!!!')
        
    def __mul__(self, partner):
        if self.status == partner and self.sex != partner.sex:
            return Human('', random.choice(['M', 'W']))
        else:
            raise Exception('They cannot make children !!!')
        
        
john = Human('John', 'm')
ann = Human('Ann', 'w')
mike = Human('Mike', 'm')
sara = Human('Sara', 'w')

john + ann
baby = john * ann

p = Point(10, 20)
p3 = Point_3d(20, 30, 40)