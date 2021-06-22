def anagram(s1, s2):
    if len(s1) != len(s2):
        print('oh')
        return False

    p = 0
    l = len(s1)

    while p < (l):
        if s1 == (s2[p:l] + s2[0:p]):
            return True
        else:
            p += 1 

    return False

print(anagram('kiragazinka', 'iragazinkak'))
