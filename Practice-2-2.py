class User:
    count = 0
    def __init__(self, name, login, password):
        self.__name__ = name
        self.__login__ = login
        self.__password__ = password
        self.__class__.count += 1

    @property
    def name(self):
        return self.__name__

    @name.setter
    def name(self, value):
        self.__name__ = value

    @property
    def login(self):
        return self.__login__
    
    @property
    def pswd(self):
        return "*********"

    @pswd.setter
    def pswd(self, value):
        self.__password__ = value

    def show_info(self):
        print(f'Name: {self.__name__}\nLogin: {self.__login__}')


class SuperUser(User):
    count = 0
    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role__ = role

    @property
    def role(self):
        return self.__role__

    @role.setter
    def role(self, value):
        self.__role__ = value

    def show_info(self):
        super().show_info()
        print(f'Role: {self.__role__}')

