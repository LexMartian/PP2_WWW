i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1          #1 2 3
    
    
i = 1
while i < 6:
    print(i)
    if i == 3:
        i += 1
    i += 1           #1 2 4 5
    
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")  #1 2 3 4 5 "i is no longer less than 6"