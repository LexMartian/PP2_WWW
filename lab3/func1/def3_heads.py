def solve(numheads, numlegs):
    rabbits = (numlegs - 2*numheads) / 2
    chickens = numheads - rabbits
    return chickens, rabbits

chickens, rabbits = solve(35, 94)
print("Num of chickens is ", chickens)
print("Num of rabbits is ", rabbits)