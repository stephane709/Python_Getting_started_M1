# natural even numbers
my_array = []
my_array.insert(0,2)
count = 1
counter = 1
while count < 50:
    my_array.insert(count, (my_array[count -1] + 2))
    count += 1
    counter += 1

print(my_array)
print(counter)



# Reversing the array
reserve_list = []
i = -1
for x in my_array:
    #print(my_array[i])
    reserve_list.insert(i, x)
    i -= 1

print(reserve_list)
