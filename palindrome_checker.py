s = input("please enter your string for testing: ")

p = s[::-1]
is_palindrome = False
for i in range(0,len(s)):
        if s[i] == p[i] :
            is_palindrome = True
        else:
            is_palindrome = False

if is_palindrome == True:
    print ("{} is a palindrome".format(s))
else:
    print ("{} is not a palindrome".format(s))
