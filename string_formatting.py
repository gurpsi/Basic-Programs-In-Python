name = input('Enter your name: ')
surname = input('Enter your surname name: ')
message = f'Hello {name} {surname}' # for python 3.6+
# OR
# message = 'Hello %s %s' % (name,surname) # for python 2 & 3
print(message)