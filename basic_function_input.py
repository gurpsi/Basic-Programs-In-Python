'''
Basic function definition with simple if else.
Asking user to input the value using: input function
'''

def temperature(i):
    if i > 7:
        return 'Warm'
    else:
        return 'Cold'

x = float(input('Enter the temperature: ')) # Converting the string value to float.
print(temperature(x))