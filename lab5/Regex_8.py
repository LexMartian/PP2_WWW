import re

def split_at_uppercase(text):
    parts = re.findall('[A-Z][^A-Z]*', text)
    return parts

# Test the function
input_string = "SplitThisStringAtUppercaseLetters"
result = split_at_uppercase(input_string)
print(result)
