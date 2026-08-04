# Write a program to mine a log file and find out whether it contains 'python'
with open("log_file.txt","r") as f:
    data=f.read()
if("python".title() in data):
        print("python is present in log file")
else:
        print("python is not present in log file")    