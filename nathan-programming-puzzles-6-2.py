import random
age = random.randint(50, 150)
x = 0

if age%2 == 0:
    while x != age:
        x = x + 1
        if x%2 == 0:
            print(x)
else:
    while x != age:
        x = x + 1
        if x%2 == 1:
            print(x)
if age > 75:
    print("Dad is %d years old" % age)
