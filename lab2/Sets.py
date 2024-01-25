fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!") #Yes, apple is a fruit!
  
fruits.add("orange") #"apple", "banana", "cherry", "orange"

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits) #"apple", "banana", "cherry","orange", "mango", "grapes"
fruits.remove("banana") #"apple", "cherry","orange", "mango", "grapes"
fruits.discard("banana") #"apple", "cherry","orange", "mango", "grapes"
