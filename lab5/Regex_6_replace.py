import re

def main():
    file_path = r'C:\Users\User\Desktop\PP2_WWW\lab5\row.txt'  # Update with your file path
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()  # Read the content of the file as a string
        
        # Define the regex pattern to match space, comma, or dot
        pattern = r'[ ,.]'
        
        # Perform the substitution, replacing space, comma, or dot with a colon
        result = re.sub(pattern, ':', file_content)
        
        # Print the modified content
        print("Modified content:")
        print(result)
        
if __name__ == "__main__":
    main()
