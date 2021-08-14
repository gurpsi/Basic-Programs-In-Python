'''
Parsing a dictionary using for loop.
'''
phone_numbers = {"John": "+3768292", "Marry": "+4239982"}

for key, value in phone_numbers.items():
    print("{} has as phone number {}".format(key, value))


# OR

for pair in phone_numbers.items():
    print("{} has as phone number {}".format(pair[0], pair[1]))