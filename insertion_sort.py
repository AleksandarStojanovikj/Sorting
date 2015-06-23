length = input("Lenght of array: ")

array = []
for i in range(0, length):
	new_number = input("#{0} ".format(i))
	array.append(new_number)


for i in range(1, length):
        temp = array[i]
        x = i - 1
        while (x >= 0) and (array[x] > temp):
            array[x+1] = array[x]
            x = x - 1
        array[x+1] = temp


print array