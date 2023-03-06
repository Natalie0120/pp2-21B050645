# Write a Python program with builtin function that accepts 
# a string and calculate the number of upper case letters and lower case letters

def cnt(str):
    cnt1=0
    cnt2=0
    for i in str:
        if int(ord(i))>=65 and int(ord(i))<=90:
            cnt1+=1
        elif int(ord(i))>=97 and int(ord(i))<=122:
            cnt2+=1
        else:
            pass
    return cnt1, cnt2

s=str(input())
print(cnt(s))