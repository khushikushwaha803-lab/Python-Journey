# Write a Python program to rename a file to "renamed_by_python.txt".
import os

old_name = "this.txt"
new_name = "renamed_by_python.txt"

if os.path.exists(old_name):
    os.rename(old_name, new_name)
    print("File renamed successfully.")
else:
    print("File does not exist.")
