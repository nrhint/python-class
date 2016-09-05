Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from random import randint
>>> money = randint(100, 5000)
>>> if money > 100 and money < 500 or money > 1000 and money < 5000:
	print("Perfect")
else:
	print("???")

	
???
>>> money
844
>>> 
