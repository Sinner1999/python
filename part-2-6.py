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

def list_of_students(lst):

    q9 = Queue()
    q10 = Queue()
    q11 = Queue()

    for n in lst:
        student = n.split()
        if student[0] == '9':
            q9.enqueue(student[1])
        elif student[0] == '10':
            q10.enqueue(student[1])
        elif student[0] == '11':
            q11.enqueue(student[1])

    print('9:')
    while q9.size() > 0:
        print(q9.dequeue())

    print('10:')
    while q10.size() > 0:
        print(q10.dequeue())

    print('11:')
    while q11.size() > 0:
        print(q11.dequeue())

class RadixSort:
    def __init__(self, n):
        self.__bins = list()
        self.__nums = n
        for i in range(10):
            self.__bins.append(Queue())

    def distribute(self, digit):
        for i in range(10):
            if digit == 1:
                self.__bins[self.__nums[i]%10].enqueue(self.__nums[i])
            elif digit == 10:
                self.__bins[(self.__nums[i] // 10) % 10].enqueue(self.__nums[i])
            elif digit == 100:
                self.__bins[self.__nums[i] // 100].enqueue(self.__nums[i])

    def collect(self):
        i = 0
        for digit in range(10):
            while self.__bins[digit].size() > 0:
                self.__nums[i] = self.__bins[digit].dequeue()
                i +=1
            
    def show(self):
        return ''.join(str(self.__nums))

names = ['Vasya', 'Zina', 'Petya', 'fedya', 'Katya', 'Ira', 'Lena'] 
# winner = hot_potato(names, 7)
# print(f'{winner} is win...')

lst = ['9 Ivanov', '10 Petrov', '9 Sidorov', '11 Fedorov', '11 Sergeev', '10 Laptev']

# list_of_students(lst)


from random import randrange

nums = []
for i in range(10):
    nums.append(randrange(1000))

rs = RadixSort(nums)

print('1: ', rs.show())
rs.distribute(1)
rs.collect()
print('2: ', rs.show())
rs.distribute(10)
rs.collect()
print('3: ', rs.show())
rs.distribute(100)
rs.collect()
print('4: ', rs.show())




