class Stack:
    def __init__(self):
        self.__data = list()

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) > 0:
            return self.__data.pop()
        return None

    def peek(self):
        if len(self.__data) > 0:
            return self.__data[len(self.__data) - 1]
        return None

    def is_empty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def show(self):
        print(', '.join(str(val) for val in self.__data))


def trains(s):
    dock = Stack()
    needed = 1
    train = list(map(int, s.split()))

    for car in train:
        dock.push(car)
        while dock.size() > 0:
            if dock.peek() == needed:
                dock.pop()
                needed += 1
            else:
                break

    if dock.is_empty():
        return "Выполнено"
    else:
        return('Невозможно')
  
print(trains(input('Wagons :')))