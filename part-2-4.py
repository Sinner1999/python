

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

    def is_empty(self):
        return self.__head is None

    def add(self, item):
        node = Node(item)
        node.set_next(self.__head)
        self.__head = node

    def size(self):
        