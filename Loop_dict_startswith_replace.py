'''
Loop over dictionary and using function startswith() and replace()
'''

phone_numbers = {"John Smith": "+3768292", "Marry Simpons": "+42399820"}
for i in phone_numbers.items():
    if i[1].startswith("+"):
        print(i[1].replace('+','00'))