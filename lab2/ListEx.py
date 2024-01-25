#List is a collection which is ordered and changeable. Allows duplicate members.

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)  #allow duplicates

thislist = ["apple", "banana", "cherry"]
print(len(thislist))  # lenth, n of elements (3)


list3 = [True, False, False] #can be any data type
list1 = ["abc", 34, True, 40, "male"]

mylist = ["apple", "banana", "cherry"]
print(type(mylist))   #<class 'list'>

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)       #create a list