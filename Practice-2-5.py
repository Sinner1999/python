class Queue:
    def __init__(self):
        self.__data = list()

    def enqueue(self, item):
        self.__data.append(item)
    
    def dequeue(self):
        if len(self.__data) > 0:
            return self.__data.pop(0)
        return None

    def rear(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data) - 1]
        return None

    def front(self):
        if len(self.__data) > 0:
            return self.__data[0]
        return None

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)
    
    def show(self):
        print(', '.join(str(val) for val in self.__data))

    def clear(self):
        self.__data = list()

class DanceFloor:
    def __init__(self, file_name):
        self.__boys = Queue()
        self.__girls = Queue()
        with open(file_name, 'r', encoding='utf-8') as fl:
            for line in fl:
                dancer = line.split()
                if dancer[0] == 'М':
                    self.__boys.enqueue(dancer[1])
                else:
                    self.__girls.enqueue(dancer[1])

    def dance(self):
        print('Образовались следующие пары:')
        while self.__boys.size() > 0 and self.__girls.size() > 0:
            print(f'{self.__girls.dequeue()} и {self.__boys.dequeue()}')

        if self.__boys.size() > 0:
            print (f'Мальчиков в очереди {self.__boys.size()} и первый из них - {self.__boys.front()}')
        elif self.__girls.size() > 0:
            print (f'Девочек в очереди {self.__girls.size()} и первая из них - {self.__girls.front()}')
        else:
            print ('Очереди нет')

