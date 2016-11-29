Python 3.4.2 (default, Oct 19 2014, 13:31:11) 
[GCC 4.9.1] on linux
Type "copyright", "credits" or "license()" for more information.
>>> from random import randint
>>> twinkes = randint(0, 750)
>>> if tinkes > 100:
	print("Too few")
elif twinkes < 500:
	print("Too many")
else:
	pass

Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    if tinkes > 100:
NameError: name 'tinkes' is not defined
>>> if twinkes > 100:
	print("Too few")
elif twinkes < 500:
	print("Too many")
else:
	pass

Too many
>>> twinkes
91
>>> if twinkes < 100:
	print("Too few")
elif twinkes >500:
	print("Too many")
else:
	pass

Too few
>>> twinkes
91
>>> 
