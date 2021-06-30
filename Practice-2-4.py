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
    st1 = Stack()
    st2 = Stack()
    st_z = Stack()
    s = s[::-1]

    for i in s.split(" "):
        print(i)
        st1.push(int(i))
    
    
    st_z.push(st1.pop())
    while True:
        
        # print(f'a = {st_z.peek()}')
        if st2.is_empty():
            if st_z.peek() == 1:
                st2.push(st_z.pop())
                print(f'in 2 === {st2.peek()}')
        else:
            if st_z.peek() == (st2.peek() + 1):
                st2.push(st_z.pop())
        # print(st2.peek())
        if st1.is_empty():
            if st_z.is_empty():
                return "Выпонено"
            elif st_z.peek() != (st2.peek() + 1):
                return "Невозможно"
        else: 
            st_z.push(st1.pop())

        print(f'1 = {st1.show()}, 2 = {st2.show()}, z = {st_z.show()}')

    # return "Невозможно"


print(trains(input('Wagons :')))