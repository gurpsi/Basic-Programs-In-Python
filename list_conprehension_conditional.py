'''
List iteration using list comprehension.
Say you want to divide all the elements by 10, with some conditions i.e. ignoring negative values.
'''
temps = [45,67,89,90,-5,20,30,50,-1]
new_temp = [i / 10 for i in temps if i > 0]
print(new_temp)