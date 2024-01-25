fruits = ["apple", "banana", "cherry"]
print(fruits[1]) #banana

fruits[0] = "kiwi" # "kiwi", "banana", "cherry"
fruits.append("orange") #"kiwi", "banana", "cherry", "orange"
fruits.insert(1, "lemon") #"kiwi","orange", "banana", "cherry", "orange"
fruits.remove("banana") #"kiwi","orange", "cherry", "orange"

print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[3:6]) #"cherry", "orange", "kiwi"
print(len(fruits)) #7