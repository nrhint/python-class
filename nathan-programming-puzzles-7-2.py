def moonWeight(weight, increace, years):
    print(weight * 0.165)
    for x in range(years):
        weight = weight+increace
        print("year " + str(x+1) + ": " + str(weight*0.165))

loop = True

while loop == True:
    w = input("weight  ")
    i = input("increace per year  ")
    y = input("years  ")
    moonWeight(w, i, y)
