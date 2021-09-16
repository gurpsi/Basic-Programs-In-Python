'''
Sorting and Up-casing the 'n' number of string values.
'''

def up(*args):
    a = list(args)
    a.sort()
    b = [i.upper() for i in a]
    return b

print(up('c','a','b'))

# OR

def foo(*args):
    args = [x.upper() for x in args]
    return sorted(args)


print(foo('c','a','b'))