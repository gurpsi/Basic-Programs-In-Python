'''
Major Operations:
'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
'''

temp = [1,7,2,4,3,5]
x = int(input('Enter value to insert in to list:'))
temp.append(x)
print(temp)

temp1 = temp.copy() # Returns the shallow copy.
'''
Shallow Copy vs Deep Copy:
Shallow copies duplicate as little as possible. 
A shallow copy of a collection is a copy of the collection structure, not the elements. 
With a shallow copy, two collections now share the individual elements.

Deep copies duplicate everything. 
A deep copy of a collection is two collections with all of the elements in the original collection duplicated.
Ref: https://stackoverflow.com/questions/184710/what-is-the-difference-between-a-deep-copy-and-a-shallow-copy

Example: https://www.programiz.com/python-programming/shallow-deep-copy
'''

x = int(input('Enter value to remove from list:'))
temp.remove(x)
print('temp:',temp)
print('temp1:',temp1)


workdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
weekend = ["Sat", "Sun"]
print('Example for extend')
workdays.extend(weekend)

