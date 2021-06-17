def anagram(s1, s2):
    if len(s1) != len(s2):
        return False
    
    a1 = list(s1).sort()
    a2 = list(s2).sort()

    return True if a1 == a2 else False
