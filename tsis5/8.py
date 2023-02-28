import re
txt=str(input())
print(re.findall('[A-Z][^A-Z]*', txt))