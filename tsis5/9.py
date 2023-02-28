import re
def space(txt):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

s=str(input())
print(space(s))