#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

thistuple = ("apple", "banana", "cherry")
print(thistuple)     #('apple', 'banana', 'cherry')

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))  #3


thistuple = ("apple",)      # <-u see the ','
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))      # no ',' = isnot tuple


tuple3 = (True, False, False)

tuple1 = ("abc", 34, True, 40, "male")

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)