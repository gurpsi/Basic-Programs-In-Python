'''
Positive Index:
    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
       0      1      2      3      4      5      6

Negative Index:
    ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
      -7     -6     -5     -4     -3     -2     -1
'''

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
# Output: ['Tue', 'Wed', 'Thu']

# First 3 Elements:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
# Output: ['Mon', 'Tue', 'Wed']

# Last 3 elemants:
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
# Output: ['Fri', 'Sat', 'Sun']

# Just leaving the last one
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1]
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']

# Just leaving the last 2
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2]
# Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']