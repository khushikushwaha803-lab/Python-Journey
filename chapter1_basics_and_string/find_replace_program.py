#chaining
letter= '''Dear <|name|>,
You are selected!
<|Date|> '''
print(letter.replace("<|name|>","geetanjali").replace("<|Date|>","23 july 2027"))
 #program to detect double space
a="i want success in   my life" 
print(a.find("  "))
#replace double space with single space
print(a.replace("  "," "))
