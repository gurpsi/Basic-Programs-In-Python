message = "hello there"

if "hello" in message:
    print("hi")
else:
    print("I don't understand")

# Multiple Conditions:
if "hello" in message:
    print("hi")
elif "hi" in message:
    print("hi")
elif "hey" in message:
    print("hi")
else:
    print("I don't understand")

# Checking conditions with 'and' operator:
x = 1
y = 1

if x == 1 and y == 1:
    print("Yes")
else:
    print("No")

# Checking conditions with 'or' operator:
if x == 1 or y == 2:
    print("Yes")
else:
    print("No")

# Check if the value is of a particular type:
isinstance("abc", str)
isinstance([1, 2, 3], list)

# OR

type("abc") == str
type([1, 2, 3]) == list