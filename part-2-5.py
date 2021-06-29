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
        print('\n'.join(str(val) for val in self.__data))


def brackets_checker(s):
    stack = Stack()

    for char in s:
        if char == '(':
            stack.push(char)
        elif stack.is_empty():
            return False
        elif char == ')':
            stack.pop()
        else:
            if stack.is_empty():
                return False

    if stack.is_empty():
        return True
    return False


def convertor(dec, dev = 2):
    allowed = '0123456789ABCDEF'
    stack = Stack()
    while dec > 0:
        stack.push(dec%dev)
        dec //= dev
    s = ''
    while not stack.is_empty():
        s += allowed[stack.pop()]
    return s

print(brackets_checker('(()(()(())))'))        
print(brackets_checker(')()(()(())))'))        
print(brackets_checker('(()(())(())))'))        


s = Stack()
s.push(10)
s.push(11)
s.push(12)
s.push(13)
s.push(14)
s.push(15)
s.push(16)
s.push(17)

print(convertor(196))
print(convertor(255))
print(convertor(56))
print(convertor(196, 8))
print(convertor(255, 8))
print(convertor(56, 8))
print(convertor(196, 16))
print(convertor(255, 16))
print(convertor(56, 16))