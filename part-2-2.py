class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point - x = "{self.x}", y = "{self.y}".'

    
    def move_to(self, x = 0, y = 0):
        self.x = x
        self.y = y
