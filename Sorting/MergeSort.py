
# O(log n)
def mergeSort(arr):
	if len(arr) <= 1:
		return arr 
	n = len(arr)
	arr1 = mergeSort(arr[: n // 2])
	arr2 = mergeSort(arr[n // 2: ])

	return merge(arr1, arr2) 

#O(arr1 + arr2) -> O(n)
def merge(arr1, arr2):
	i = 0
	j = 0
	m = []
	while i < len(arr1) and j < len(arr2):
		if arr1[i] <= arr2[j]:
			m.append(arr1[i])
			i += 1
		else:
			m.append(arr2[j])
			j += 1

	while i < len(arr1):
		m.append(arr1[i])
		i += 1 

	while j < len(arr2):
		m.append(arr2[j])
		j += 1

	return m

arr = list(map(int, input().split()))

print(*mergeSort(arr))