# Function

name = input("What's your name?")

birthday = input("Is today your birthday?")


def happy_birthday(n):
    print("Happy Birthday to you " + n + "!!")


if birthday == "Yes" or birthday == "yes":
    happy_birthday(name)
else:
    print("Sorry, come again when it's your birthday " + name + ".")
