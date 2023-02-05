string = 'you shall not pass'
split_str = string.split(' ') # split on spaces
reversed_str = reversed(split_str) # reverse words
final_str = ' '.join(reversed_str) # join the reversed words back to string
print("Reversed string: " , final_str)