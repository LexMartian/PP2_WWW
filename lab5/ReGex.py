import re

"""
[a-z]           a set of characters
\d              escape special characters
.               any character 'he..o'
^               starts with 'ello'
$               ends with 'world$'
*               Zero or more occurrences  "he.*o"
+               One or more occurrences "he.+o"
?               Zero or one occurrences
{}              Exact number of occurrences "he.{2}o"
|               Either or   "falls|stays"
()              Capture and group

"""
def main():
    file_path = r'C:\Users\User\Desktop\PP2_WWW\lab5\row.txt'
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.readlines()
        
        pattern = r'' 
        
        for line in file_content:
            matches = re.findall(pattern, line) 
            if matches:
                print("Found match in line:", line.strip()) 

if __name__ == "__main__":
    main()
    
    
"""
1) ab*
2) abb|abbb
3) [a-z]+_[a-z]+
4) \b[A-Z][a-z]+
5) (a).*b$
"""
