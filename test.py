print("hello world")

x = 10
print(type(x))

x = 0.1
print(type(x))

a = 10
b = 2
x = a + b / b * 2**a
print(x)

x = "string"
print (type(x))

y = "also a string"
print (type(y))

z = "m"
print (type(z))

my_string = "The little brown fox"
print(my_string[0:10])
print(my_string[0:3])
print(my_string[17:21])
print(my_string[4:10])
print(my_string).upper()
print(my_string).title()
print(my_string[11:])
print(my_string[8:16]).title()
print(my_string[9::-1]).lower()

shopping = ["bread", 1, 2, 3, "butter"]
print(type(shopping))

shopping = ["bread", "butter", "ham"]
print(type(shopping))

shopping = ["bread", "butter", "ham"]
shopping.append("milk")
print(shopping)

shopping = ["bread", "butter", "ham"]
print("ham" in shopping)
print(shopping[1])
shopping[0] = "milk"
print(shopping)

shopping = ["bread", "butter", "ham"]
shopping.pop()
print(shopping)

shopping = ["bread", "butter", "ham"]
shopping.pop(1)
print(shopping)

student = ("Ian", 20, "Maths")
print(type(student))

s = {1, 2, 2, 3, 3}
print(s)
print(type(s))

shopping = ["bread", "ham", "cheese", "bread"]
print(set(shopping))
print(list(set(shopping)))

country_codes = {"US": "United States", "UK": "United Kingdom"}
print(type(country_codes))
print(country_codes.get("US"))

country_codes['Fr'] = 'FRANCE'
print(country_codes)