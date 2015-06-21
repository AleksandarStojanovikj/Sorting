length = input("Lenght of array: ")

array = []
for i in range(0, length):
	new_number = input("#{0} ".format(i))
	array.append(new_number)


# Nadole ti ja resavas zadacata, sortiraj gi site broevi so bubble sort
for x in range(0, length-1):
	for i in range(0, length-1):
		if array[i] > array[i+1]:
			temp = array[i]
			array[i] = array[i+1]
			array[i+1] = temp

print array