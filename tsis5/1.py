import re
def mystring(txt):
    pattern='^a(b*)$'
    if re.search(pattern, txt):
        print('A match is found')
    else:
        print('Not found')

s=str(input())
print(mystring(s))