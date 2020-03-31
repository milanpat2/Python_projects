print("Write a Python function to sum and multiply all the user given numbers")
print("")

input_list = input("Enter all the numbers with comma in between: ")
lst = input_list.split(",")
sum_multiply = int(input("Enter 1 for sum and 2 for multiplication and 3 for both the results: "))

def sumOfTheList():
    sum = 0
    for x in lst:
        sum += int(x)
    return sum


def multiplicationOfTheList():
    mult = 1
    for x in lst:
        mult *= int(x)
    return mult


if sum_multiply == 1:
    print("sum:", sumOfTheList())
elif sum_multiply == 2:
    print("multiplication:", multiplicationOfTheList())
elif sum_multiply == 3:
    print("sum:", sumOfTheList())
    print("multiplication:", multiplicationOfTheList())