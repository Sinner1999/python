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

    
def hot_potato(names, num):
    queue =Queue()
    for name in names:
        queue.enqueue(name)
    queue.show()   

    eliminated = ''

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        eliminated = queue.dequeue()
        print(f'{eliminated} is out')
        queue.show()

    return queue.dequeue()


names = ['Vasya', 'Zina', 'Petya', 'fedya', 'Katya', 'Ira', 'Lena'] 
winner = hot_potato(names, 7)
print(f'{winner} is win...')

