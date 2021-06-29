

class Node:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def set_next(self, node):
        self.__next = node

    def get_next(self):
        return self.__next


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        if self.__tail is None:
            self.__tail = node
        node.set_next(self.__head)
        self.__head = node

    def size(self):
        current = self.__head
        count = 0
        while current is not None:
            current = current.get_next()
            count +=1
        return count

    def search(self, item):
        current = self.__head
        while current is not None:
            if current.get_data() == item:
                return True
            current = current.get_next()
        return False

    def __str__(self):
        if self.__head is None:
            return '[]'
        current = self.__head
        out = '[' + str(current.get_data())
        while current.get_next() is not None:
            current = current.get_next()
            out += ', ' + str(current.get_data())
        out += ']'
        return out

    def remove(self, item):
        current = self.__head
        prev = None
        while not current is None:
            if current.get_data() == item:
                if prev is None:
                    self.__head = current.get_next()
                else:
                    prev.set_next(current.get_next())    
                return True
            prev = current
            current = current.get_next()
        return False 

    def append(self, item):
        node = Node(item)
        if self.__head is None:
            self.__head = node
        current = self.__tail
        current.set_next(node)
        self.__tail = node
        

    def insert(self, item):
        pass

    def index(self, pos, item):
        if self.__head is None:
            return -1
        current = self.__head
        pos = 0
        while current is not None:
            if current.get_data() == item:
                return pos
            current = current.get_next()
            pos += 1
        return False

    def pop(self):
        pass



ml = LinkedList()
ml.add(10)
ml.add(15)
ml.add(25)
ml.add(34)
ml.add(54)
ml.add(84)
ml.add(65)
        