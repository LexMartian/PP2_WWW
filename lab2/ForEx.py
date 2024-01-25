#A for loop is used for iterating over a sequence

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  
  
#Loop through the letters in the word "banana":
for x in "banana":
  print(x)


#Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
  
  
#With the continue statement we can stop the current iteration of the loop,
#and continue with the next:
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(2):       #print from 0 to 6, excluding 6
  print(x)
  
for x in range(1, 3):    ##print from 0 to 6, excluding 6
  print(x)


#Increment the sequence with 3 (default is 1):
for x in range(2, 10, 3):
  print(x)
  
  
#Print each adjective for every fruit:

adj = ["red", "big"]
fruits = ["apple", "banana"]

for x in adj:
  for y in fruits:
    print(x, y)