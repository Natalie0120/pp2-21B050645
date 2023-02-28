from re import sub
def tosnake(txt):
    return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',
    sub('([A-Z]+)', r' \1',
    txt.replace('-', ' '))).split()).lower()

s=str(input())
print(tosnake(s))