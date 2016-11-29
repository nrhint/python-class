import sys
def moonWeight():
    w = input("weight  ")
    i = input("increace per year  ")
    y = input("years  ")
    print(w * 0.165)
    for x in range(y):
        w = w+i
        print("year " + str(x+1) + ": " + str(w*0.165))
        
loop = True

while loop == True:
    moonWeight()
