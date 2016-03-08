x = True and True
print(x)

x = False and False
print (x)

x = 1 == 1
print (x)

x = 2 == 1
print (x)

x = 1 != 2
print (x)

x = not True
print (x)

x = 10 == 1 or 1 == 1
print (x)

x = False and 0!= 0
print (x)

x = True or 1 == 1
print (x)

x = "test" == "testing"
print (x)

x = 1 != 0 and 2 == 1
print (x)

x = "test" != "testing"
print (x)

x = "test" == 1
print (x)

x = not (True and False)
print (x)

x = (1 == 1 and 0 != 1)
print (x)

x = (10 == 1 or 1000 == 1000)
print (x)

x = (1 != 10 or 3 == 4)
print (x)

x = ("testing" == "testing" and "Zed" == "Cool Guy")
print (x)

x = 1 == 1 and (not ("testing" == 1 or 1 == 0))
print (x)

x = "chunky" == "bacon" and (not (3 == 4 or 3 == 3))
print (x)

x = 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))
print(x)

primes = [2, 3, 5, 7]
for prime in primes:
	print(prime)

name = "Jack"
for character in name:
		print (character)

count = 0
while count < 5:
	print(count)
	count += 1

count = 0
while True:
	print(count)
	count += 1
	if count >= 5:
		break