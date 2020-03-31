print("Write a program which can compute the factorial of a given numbers")
print("The results should be printed in a comma-separated sequence on a single line.")
print("Suppose the following input is supplied to the program:8")
print("Then, the output should be:40320")
print("")


def fact(a):

    factorial = 1

    if a == 0:
        return 1
    else:
        for i in range(1, a+1):
            factorial = factorial*i
        print(factorial)


fact(5)

