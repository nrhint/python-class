from random import randint

ninjas = randint(0, 75)

if ninjas < 50:
    print("Too many")
elif ninjas < 30:
    print("It will be a strugle, but I can do it")
else ninjas < 10:
    print("I can fight those ninjas")

print()
print(ninjas)
