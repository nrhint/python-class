def moonWeight(weight, increace):
    print(weight * 0.165)
    for x in range(0, 15):
        weight = weight+increace
        print("year " + str(x+1) + ": " + str(weight*0.165))

loop = True

while loop == True:
    w = input("weight  ")
    i = input("increace per year  ")
    moonWeight(w, i)
