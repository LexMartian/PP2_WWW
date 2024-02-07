import math
def vol_of_sphere(rad):
    vol = (4/3) * math.pi * rad**3
    return vol
    
radius = float(input("Radius: "))
vol = vol_of_sphere(radius)
print("Vol of sphere is %0.3f" % vol)