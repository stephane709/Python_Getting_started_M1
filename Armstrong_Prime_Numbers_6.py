#def no_of_digits(a):
#   i = 0
#   while a > 0:
#       a //= 10 
#        i+=1
#    return i

Input = int(input("Enter a number of your choice "))



def sum_of_digit(num):
    length = len(str(num))
    sum = 0
    while num > 0:
        digit = num % 10
        num //= 10
        sum += pow(digit, int(length))
    return sum


def prime(num):
    for x in range(2 , num // 2):
        if (num % x) == 0:
            x = print("Is not prime")
            break
        else: 
            x = print("Is prime")
            return x


prime(5)

if(sum_of_digit(Input) == Input):
    print("Your input in an armstrong number")
else:
    print("Not an armstrong number")

