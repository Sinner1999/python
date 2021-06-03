class Lamp:

    count = 0
    
    def __init__(self, floor):
        self.__state = False
        self.__floor = floor
        Lamp.count += 1

    def __repr__(self):
        return f'lamp on {self.floor} floor is {"On" if self.state else "Off" }'

    def get_state(self):
        return self.__state

    def get_floor(self):
        return self.__floor

    def set_floor(self):
        return self.__floor

    state = property(get_state)
    floor = property(get_floor, set_floor )

    def switch_on(self):
        if self.__state == False:
            self.__state = True
            print('On')

    def switch_off(self):
        if self.__state:
            self.__state = False
            print('Off')

lamp1 = Lamp(2)
lamp2 = Lamp(3)
lamp3 = Lamp(1)
lamp4 = Lamp(1)

lamp1.switch_on()
lamp1.switch_off()

print(lamp1.state)
print(lamp1.floor)
print(Lamp.count)



