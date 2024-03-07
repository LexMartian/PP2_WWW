import re

def main():
    file_path = r'C:\Users\User\Desktop\PP2_WWW\lab5\row.txt' 
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()
        
        pattern = r'[ ,.]'
        
        result = re.sub(pattern, ':', file_content)
        
        print("Modified content:")
        print(result)
        
if __name__ == "__main__":
    main()
