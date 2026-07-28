def reverse_string_recurssion(s):
    if(len(s)==0):
        return s
    return reverse_string_recurssion(s[1:])+s[0]

print(reverse_string_recurssion("harry"))