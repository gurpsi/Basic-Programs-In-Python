'''
For Keyword args we use double asterisk '**'.
And it is returned as a 'dict' i.e. with a key value pair.
'''

def sum_kargs(**kargs):
    return sum(kargs.values())

print(sum_kargs(a=1,b=2))


# Find winner with max score

def find_winner(**kwargs):
    return max(kwargs)


print(find_winner(Andy=17, Marry=19, Sim=45, Kae=34))