# Python Barista Bot

# introduction
print("Hello, welcome to Nas Brews!!\n")

# variables
menu = """- Coffee
- Tea
- Milk
- Water
- Espresso"""

# start of code

name = input("What's your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you evil?\n")
    g_deeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" or evil_status == "yes" and g_deeds < 4:
        print("Get out of here " + name + "!!")
        exit()
    else:
        print("So you're one of those good " + name + "'s, come on in!!\n")
else:
    print("\nHello " + name + ", thank you for coming in today!")

drink = input(
    "\nSo " + name + ", what would you like today?\n \nWe have:\n" + menu + "\n\nWhich of these entices you the most?\n")

# Using only if and else statements
# if drink == "Espresso" or drink == "espresso":
#  price = 11
# else:
#  if drink == "Coffee" or drink == "coffee":
#    price = 9
#  else:
#    if drink == "Tea" or drink == "tea":
#      price = 7
#    else:
#      if drink == "Milk" or drink == "milk":
#        price = 5
#      else:
#        if drink == "Water" or drink == "water":
#          price = 2
#        else:
#          print("Sorry, we don't have that here.")
#          exit()


# Using if, elif, and else statements
if drink == "Espresso" or drink == "espresso":
    e_cream = input("Would you like whipped cream?\n")
    if e_cream == "Yes" or e_cream == "yes":
        price = 14
    else:
        price = 11
elif drink == "Coffee" or drink == "coffee":
    price = 9
elif drink == "Tea" or drink == "tea":
    price = 7
elif drink == "Milk" or drink == "milk":
    price = 5
elif drink == "Water" or drink == "water":
    price = 2
else:
    print("Sorry, we don't have that here.")
    exit()

amount = input("\nHow many " + drink + "'s would you like?\n")

total = price * int(amount)

print("\nThank you, your total is: $" + str(total))

# template with plural always
# print("\nNice choice, your " + amount + " " + drink + "'s will be ready in a few moments.")


# prints with plural if amount is greater than 1
if int(amount) > 1:
    print("\nNice choice, your " + amount + " " + drink + "'s will be ready in a few moments.")
else:
    print("\nNice choice, your " + drink + " will be ready in a few moments.")
