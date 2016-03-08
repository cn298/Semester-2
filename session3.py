def max_of_two(x, y):
	if x > y:
		return x
	return y
def max_of_three(x, y, z):
	return max_of_two(x, max_of_two(y, z))
print(max_of_three(3, 6, -5))

def sum(numbers):
	total = 0
	for x in numbers:
		total += x
	return total
print(sum((8, 2, 3, 0, 7)))

def multiply(numbers):
	total = 1
	for x in numbers:
		total *= x
	return total
print(multiply((8, 2, 3, -1, 7)))

def string_reverse(str1):
	rstr1 = ''
	index = len(str1)
	while index > 0:
		rstr1 += str1[index - 1]
		index = index - 1
	return rstr1
print(string_reverse('1234abcd'))

def factorial(n):
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)
n = int(input("1"))
print(factorial(n))

def test_range(n):
	if n in range(3, 9):
		print(" %s is in the range"%str(n))
	else:
		print("The number is outside the given range")
test_range(5)

def string_test(s):
	d={"UPPER_CASE":0, "LOWER_CASE":0}
	for c in s:
		if c.isupper():
			d["UPPER_CASE"]+=1
		elif c.islower():
			d["lOWER_CASE"]+=1
		else:
			pass
			