import re
def tocamel(txt):
    return ''.join(x.capitalize() or '_' for x in txt.split('_'))

s=str(input())
print(tocamel(s))