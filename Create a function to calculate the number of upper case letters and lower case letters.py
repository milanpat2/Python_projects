print("Write a Python function that accepts a string and")
print("calculate the number of upper case letters and lower case letters")

str = input("Enter input string: ")


def lowerUpperCaseCount():

    lowercase = 0
    uppercase = 0

    for c in str:
        if c.islower():
            lowercase += 1
        else:
            uppercase += 1
    print("lowercase characters:", lowercase)
    print("uppercase characters:", uppercase)


lowerUpperCaseCount()



