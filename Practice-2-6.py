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
    def _parse(self):
        pass

    @abc.abstractmethod
    def _evaluate(self):
        pass

class Interpreter(InterpreterAbstract):
    def __init__(self, code):
        self.__code = code
        self.__nums = Stack()
        self.__oper = Stack()

    def execute(self):
        return self._parse()

    def _parse(self):
        nums = '0123456789'
        opers = '()+-*/^'

        for char in self.__code:
            if char == ')':
                self._evaluate()
                print(')')
            else:
                if char in nums:
                    self.__nums.push(int(char))
                elif char in opers:
                    self.__oper.push(char)
        return self.__nums.pop()
        
    def _evaluate(self):
        a = self.__nums.pop()
        while self.__oper.peek() != '(':
            b = self.__nums.pop()
            c = self.__oper.pop()
            print(a, b)
            if c =="+":
                a = a + b
            elif c =="-":
                a = a - b
            elif c =="*":
                a = a * b
            elif c =="/":
                a = a // b
            elif c =="^":
                a = a ** b
        c = self.__oper.pop()
        self.__nums.push(a)



inp = Interpreter('(1+2-(3*4)/(5^6+(7-8))*9)')
print(inp.execute())
