'''
Return the list of elements if it is int type.
'''

def foo(x):
    return [i for i in x if type(i) == int]
    # OR
    # return [i for i in x if isinstance(i, int)]

n = foo([99,'no data'])
print(n)