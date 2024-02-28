import re

def snake_to_camel(snake_case_str):
    words = snake_case_str.split('_')  # Split the snake case string into words
    camel_case_str = words[0] + ''.join(word.capitalize() for word in words[1:])  # Capitalize each word except the first one
    return camel_case_str


def main():
    file_path = r'C:\Users\User\Desktop\PP2_WWW\lab5\row.txt'  # Update with your file path
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()  # Read the content of the file as a string
        
        # Replace spaces, commas, and dots with a colon
        replaced_content = re.sub(r'[ ,.]', ':', file_content)
        
        # Convert snake case string to camel case string
        camel_case_content = snake_to_camel(replaced_content)
        
        print("Camel case content:")
        print(camel_case_content)

if __name__ == "__main__":
    main()
