'''
Objective is to print out all the integer value numbers from list.
'''
colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
for i in range(len(colors)):
    if isinstance(colors[i], int):
        print(colors[i])