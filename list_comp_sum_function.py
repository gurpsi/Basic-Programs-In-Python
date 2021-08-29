'''
Return the sum of list string type float values
'''

def foo2(lst):
    return sum([float(i) for i in lst])

lst = ['2.1','3.2','99.1','90.2','200.1']
print(foo2(lst))
