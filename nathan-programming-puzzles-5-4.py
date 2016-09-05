from random import randint

ninjas = randint(0, 75)

if ninjas >= 50:
    print("%d ninjas is too many!" % ninjas)
elif ninjas >= 30 and ninjas < 49:
    print("%d ninjas will be a strugle, but I can do it" % ninjas)
else:
    print("I can fight %d ninjas no probolem" % ninjas)

#print('')
#print(ninjas)
