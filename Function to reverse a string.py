print("Write a Python program to reverse a string.")


inputString = str(input("Enter the string: "))
reverseString = ""
str = len(inputString)


def reverse(inputString1): #Create afunction
    reverseString1 = ""  #Create a variable with null value
    str1 = len(inputString1) #String length
    while str1 > 0:  #Check the condition
        reverseString1 = reverseString1 + inputString1[str1 - 1] #Store the index value
        str1 = str1 - 1 #for reverse start
    print(reverseString1) #Print all store values


reverse("python")





