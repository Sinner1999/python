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
    def __init__(self, code, file):
        self.__code = code
        self.__file = file

    def execute(self):
        return self._parse()

    @abc.abstractmethod
    def _parse(self):
        pass

    @abc.abstractmethod
    def _evaluate(self):
        pass

class Interpreter(InterpreterAbstract):
    def __init__(self, code = None, file = None):
        self.__code = code
        self.__file = file
        self.__nums = Stack()
        self.__oper = Stack()
        self.__out = []

    def execute(self):
        if self.__code is not None:
            self.__out.append(self._parse())
        if self.__file is not None:
            with open(self.__file, 'r', encoding='utf-8') as f:
                for line in f:
                    self.__code = line
                    print(self.__code)
                    self.__out.append(self._parse())

        return self.__out

    def _parse(self):
        if self._validate():
            raise ValueError('Что-то не то со скобками')
        nums = '0123456789'
        opers = '(+-*/^'
        if self.__code[0] != '(':
            self.__oper.push('(')
            self.__code += ')' 

        for char in self.__code:
            if char == ')':
                print(self.__oper.peek() +' )')
                self._evaluate()
            else:
                if char in nums:
                    self.__nums.push(int(char))
                elif char in opers:
                    self.__oper.push(char)
        print(self.__oper.peek())
        # self._evaluate()
        return self.__nums.pop()
        
    def _evaluate(self):
        a = self.__nums.pop()
        while self.__oper.peek() != '(':
            b = self.__nums.pop()
            c = self.__oper.pop()
            print(b, a)
            if c =="+":
                a = b + a
            elif c =="-":
                a = b - a
            elif c =="*":
                a = b * a
            elif c =="/":
                a = b // a
            elif c =="^":
                a = b ** a
        c = self.__oper.pop()
        self.__nums.push(a)

    def _validate(self):
        a = 0
        for char in self.__code:
            if char == '(':
                a += 1
                print(a)
            elif char == ')':
                a -= 1
                print(a)
        print(a)
        return a
        




# inp = Interpreter('(1+2-(3^4)/(5+6+(7-8))*9)')
# inp = Interpreter('(1+((2+3)*(4*5)))')
inp = Interpreter(code = '2 + (dfhgdfgd ( 2 * 3 dhfjft) / ( 4 dhrtyhrt^ 5 )edrtedrt )  ', file = 'code.txt')
print(inp.execute())
