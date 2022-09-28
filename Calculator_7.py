x, y = input("Enter 2 values of your choice ").split()

first_value = int(x)
second_value = int(y)


User_option = int(input(''' Select your operation between 1 to 4:

                     1 - Addition
                     2 - Subtraction
                     3 - Multiplication
                     4 - Division
                    '''))

print(User_option)

def addition(a,b):
    return a + b

def Subtraction(a,b):
    return a - b

def Multiplication(a,b):
    return a * b

def division(a,b):
    return a // b

print(addition(first_value , second_value))


if (User_option == 1):
    add = addition(first_value , second_value)
    print("The sum of your 2 numbers is: " + str(add) )
elif (User_option == 2):
    print("The difference of your 2 numbers is: " + str(Subtraction(first_value , second_value)))
elif (User_option == 3):
    print("The Product of your 2 numbers is: " + str(Multiplication(first_value , second_value)))
elif (User_option == 4):
    print("The division of your 2 numbers is: " + str(division(first_value , second_value)))
 #else:
       # print("Wrong input, enter a number between 1 and 4")
    