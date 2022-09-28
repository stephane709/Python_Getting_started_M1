Value = int(input("Enter a number of your choice "))

first_term = 0
second_term = 1
count = 0

if (Value == first_term):
    print("fibonacci sequence is")
    print(first_term)
elif (Value == second_term):
    print("Fibonacci sequence is: \n " + str(first_term) + " , " + str(second_term))
else:
    print("Fibonacci Sequence:")
    while (count < Value):
        print(first_term)
        num = first_term + second_term
        first_term = second_term
        second_term = num
        count += 1
    