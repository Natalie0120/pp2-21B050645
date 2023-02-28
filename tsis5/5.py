import re
def myf(txt):
    pattern='a.*?b$'
    if re.search(pattern, txt):
        print('Found')
    else:
        print('Not found')

s=str(input())
print(myf(s))