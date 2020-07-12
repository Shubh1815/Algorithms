from random import randint

#O(log n)
def quickSort(arr, l, r):      
	if l >= r:
		return
	p = randint(l, r)
	arr[l], arr[p] = arr[p], arr[l]

	m = partition(arr, l, r)
	quickSort(arr, l, m - 1)
	quickSort(arr, m + 1, r)

	return

# O(n)
def partition(arr, l, r):       
	i = l + 1
	j = l
	while i <= r: 
		if arr[i] < arr[l]:
			arr[j + 1], arr[i] = arr[i], arr[j + 1]
			j += 1
		i += 1

	arr[l], arr[j] = arr[j], arr[l]
	return j

arr = list(map(int, input().split()))
quickSort(arr, 0, len(arr) - 1)
print(*arr)