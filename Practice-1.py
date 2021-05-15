import random

slovo = ['книга','месяц','ручка','шарик','олень','носок']
m = True;
5

while m:
    
    s = slovo[random.randrange(6)]
    t = {i: '0' for i in s}
    l = input("Сложность (1, 2, 3)")
    if l == '1':
        lives = 7
    elif l == '2':
        lives = 5
    else:
        lives = 3
    
    while '0' in list(t.values()) and lives > 0:
        for i in list(t.values()):
            if i == '0':
                out = '\u274E'
            else:
                out = i
            print(out, end='')
        
        inp = input('| ' + '\u2618'*lives + '   вводи тут :')
        
        if inp in list(t.keys()):
            t[inp] = inp
        elif inp == '':
            print('Надо что-то ввести')
        elif inp == s:
            for j in list(t.keys()):
                t[j] = j
        else:
            lives -= 1
            print(f'Нет такой буквы. Осталось {lives} жизней.....')
        
    if '0' in list(t.values()):
        print('Looser !!!!')
    else:
        print('Угадал !!!!!')
    m = int(input('Исчо? (да-1/нет-0) :'))

# print(s, t)