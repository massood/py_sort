
l = [7, 5, 6, 1, 2, 4, 3]

def sort(arr):
	for n in range(len(arr), 1, -1):
		for i in range(1, n):
			if (arr[i-1] > arr[i]):
				arr[i-1], arr[i] = arr[i], arr[i-1]


print ("before sorting: ")
print (l)

sort(l)

print ("the sorted array: ")
print (l)
