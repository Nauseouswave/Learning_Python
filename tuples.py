alist = ["Nas", "Nauseous", 0o06]

alist[0] = "NQ"

atuple = ("Nas", "Nauseous", 0o06)

# atuple[0] = "NQ"

print(alist)

# Lists are slower and are used for changeable data such as a list of names or numbers

favorite_food = ["Pizza", "Chocolate", "Cheese"]

# Tuples are faster and are used for different types of data like names + age

client_info = ("John", 24, "Realtor")

# You can unpack tuples

nauseouswave = ("Nas", 17, "Matcha")

# Can also be done with lists
(nickname, age, drink) = nauseouswave

print(nickname)
print(age)
print(drink)

# Tuples do not need paranthesis

totallyatuple = 1, 2, 3

print(type(totallyatuple))
print(totallyatuple)
