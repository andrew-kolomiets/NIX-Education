def swap(txt):
    '''
    >>> half("abcd"))
    cdab
    '''
    return txt[int(len(txt)/2):] + txt[:int(len(txt)/2)]

def average(*numbers):
    '''
    >>> average(2, 4, 6)
    4
    '''
    s = 0
    c = 0
    for n in numbers:
        s += n
        c += 1
    return s/c

print(50*'*') ############################################

print(swap('wkuteip'))

print(50*'*') ############################################

print(average(1, 3, 3))

print(50*'*') ############################################
