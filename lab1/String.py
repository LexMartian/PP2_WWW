x = "Hello World"
print(len(x))

txt = "Hello World"
y = txt[0]
print(y)

y = txt[2:5]
print(y)

y = txt.strip()
print(y)

y = txt.upper()
y = txt.lower()
y = txt.replace("H", "J")

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))