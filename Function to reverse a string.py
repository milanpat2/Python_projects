print("Write a Python program to reverse a string.")


inputString = str(input("Enter the string: "))
reverseString = ""
str = len(inputString)


def reverse(): #Create afunction
    reverseString = ""  #Create a variable with null value
    str1 = len(inputString) #String length
    while str1 > 0:  #Check the condition
        reverseString = reverseString + inputString[str1 - 1] #Store the index value
        str1 = str1 - 1 #for reverse start
    print(reverseString) #Print all store values


reverse()





