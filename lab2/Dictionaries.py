car =  {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model")) #Mustang

car["year"] = 2020 # "year": 2020
car["color"] = "red" #new key "color" with value "red"
car.pop("model") #remove key color
car.clear() #clear whole dict