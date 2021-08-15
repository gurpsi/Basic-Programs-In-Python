'''
Creating a function to take an input till the user inputs '\end'.
Then if it starts with question then add a Question mark.
If it is not capitalized then capitilize and add a full stop at the end.
At last once user enters '\end' display all the previously entered texts.
'''
def sentence(phrase):
    ques = ('how', 'what', 'why', 'when')
    capitalized = phrase.capitalize()
    if phrase.startswith(ques):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)

print(sentence('how are you'))

result = []
while True:
    usr_ip = input('Say Something: ')
    if usr_ip != '\end':
        result.append(sentence(usr_ip))
    else:
        break

ans = ' '.join(result)  # Concatenate string
print(ans)