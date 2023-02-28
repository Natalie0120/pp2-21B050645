import re
def mystring(txt):
    pattern='ab{2,3}'
    if re.search(pattern, txt):
        print('A match is found')
    else:
        print('Not found')

s=str(input())
print(mystring(s))