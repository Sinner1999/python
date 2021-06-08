class User:
    count = 0
    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        self.__class__.count += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def login(self):
        return self.__login
    
    @property
    def pswd(self):
        return "*********"

    @pswd.setter
    def pswd(self, value):
        self.__password = value

    def show_info(self):
        print(f'Name: {self.__name}\nLogin: {self.__login}')


class SuperUser(User):
    count = 0
    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role
        #SuperUser.count += 1
        #User.count -= 1

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    def show_info(self):
        super().show_info()
        print(f'Role: {self.__role}')

