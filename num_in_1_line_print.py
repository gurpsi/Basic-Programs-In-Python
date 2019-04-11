'''
Read an integer and print upto that number in one line.
'''


if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i, end='')
