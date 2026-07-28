def pallindrome(s):
    left=0
    right=len(s)-1
    while left<right:
        if(s[left]!=s[right]):
            return False
        left+=1
        right-=1
        return True
string="madam"
if pallindrome(string):
    print(f"{string} is a pallindrome")
else:
     print(f"{string} is not a pallindrome")   

# string="geetanjali"
# reverse_string="".join(reversed(string))
# print(reverse_string)     




   