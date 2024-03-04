import re

def insert_spaces(text):
    modified_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return modified_text


input_string = "ThisIsStringWithWordsStartingWithCapitalLetters"
result = insert_spaces(input_string)
print("Modified text:", result)