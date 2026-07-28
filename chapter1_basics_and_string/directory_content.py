# write a pyhton program to run the content of directory using OS module

import os

contents = os.listdir()

print("Contents of the current directory:")
for item in contents:
    print(item)