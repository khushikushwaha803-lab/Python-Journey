#This program checks if the word "Harry" is present in a given post or not.
post=input("enter the post :")
if("Harry".lower() in post.lower()):
    print("Harry is present in post")
else:
    print("Harry is not in th post")