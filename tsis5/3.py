import re
def myf(txt):
    pattern='^[a-z]+_[a-z]+$'
    if re.search(pattern, txt):
        print('Found')
    else:
        print('Not found')

s=str(input())
print(myf(s))