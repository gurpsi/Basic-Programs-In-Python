'''Program to find the prime numbers in an interval'''
n = input("Enter the start: ")
n = int(n)
m = input("Enter the end: ")
m = int(m)

for i in range(n,m+1):
    if (i>1):
        for j in range(2,i):
            if(i%j == 0):
                break
        else:
            print(i)