#Set is a collection which is unordered, unchangeable*, and unindexed.
#No duplicate members.

thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)        #1 = True

print(len(thisset))   # 5

set3 = {True, False, False}
set1 = {"abc", 34, True, 40, "male"}

myset = {"apple", "banana", "cherry"}
print(type(myset))    #class 'set'

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)