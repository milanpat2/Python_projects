print("Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5")
print("between 2000 and 3200 both included")
print("The numbers obtained should be printed in a comma-separated sequence on a single line")
print("")


for i in range(20, 32):
    l = list()
    if i % 7 == 0 and i % 5 != 0:
        print(i)


