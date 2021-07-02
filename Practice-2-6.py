import abc

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

class InterpreterAbstract(abc.ABC):
    def __init__(self, code):
        self.__code = code

    def execute(self):
        return self.__parse()

    @abc.abstractmethod
    def __parse(self):
        pass

    @abc.abstractmethod
    def __evaluate(self, code):
        pass

class Interpreter(InterpreterAbstract):
    def __init__(self, code):
        self.__code = code
        self.__nums = Stack()
        self.__oper = Stack()

    def execute(self):
        return self.__parse()

    def __parse(self):
        nums = '0123456789'
        opers = '()+-*/^'
        for char in self.__code:
            if char == ')':
                self.__evaluate()
            else:
                if char in nums:
                    self.__nums.push(char)
                elif char in opers:
                    self.__oper.push(char)
        

    def __evaluate(self, code):
        pass
    