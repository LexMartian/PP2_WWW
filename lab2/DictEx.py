#Dictionary is a collection which is ordered** and changeable.
#No duplicate members.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)      #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

print(thisdict["brand"])    #Ford

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)      #latest value will override

print(len(thisdict)) #3

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}                    #any datatype

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
