def reverse_string(s):
        result=""
        for char in s:
            result=char+result
        return result

string="geetanjali"
print(reverse_string(string))