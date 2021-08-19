'''
List iteration using list comprehension.
Say you want to divide all the elements by 10, with some conditions
i.e. ignoring negative values and replacing them with -1.
'''

def foo(lst):
    return [i/10 if i > 0 else -1 for i in lst]
# If we use if & else then we first write the condition then the loop.

temps = [45,67,89,90,-5,20,30,50,-1]
print('with foo: ',foo(temps))

'''
foo1 replaces the non int values to 0.
'''
def foo1(x):
    return [i if isinstance(i,int) else 0 for i in x]

temp = [45,67,89,'no data',90,-5,20,30,50,-1,'no data']
print('with foo1: ',foo1(temp))




