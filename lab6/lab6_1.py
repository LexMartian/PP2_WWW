import os
path = r'C:\Users\User\Desktop\PP2_WWW\\'
print("Only directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ])
#Если директория (файл) то принт
print("\nOnly files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ])
#Если не директория, а док то принт
print("\nAll directories and files :")
print([ name for name in os.listdir(path)])
