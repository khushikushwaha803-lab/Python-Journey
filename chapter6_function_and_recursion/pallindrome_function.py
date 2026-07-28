def is_pallindrome(s):
    return s==s[::-1]
string="radar"
if(is_pallindrome(string)):
    print(f"{string} is a pallindrome")
else:
    print(f"{string} is not a pallindrome")    

