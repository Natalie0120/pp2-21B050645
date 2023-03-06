#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

def ispalindrome(str):
	left = 0
	right= len(str) - 1
	
	while right >= left:
		if not str[left] == str[right]:
			return False
		left += 1
		right-= 1
	return True

s=str(input())
print(ispalindrome(s))