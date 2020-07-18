def linear(arr, n):

	# O(n)
	for i in range(len(arr)):
		if arr[i] == n:
			return i + 1
	return -1

def binary(arr, n):
	arr = sorted(arr)
	l = 0
	r = len(arr) - 1
	# O(log n)
	while l <= r:
		m = (l + r) // 2
		if arr[m] == n:
			return 'Element is present'
		elif arr[m] < n:
			l = m + 1
		else:
			r = m - 1

	return 'Element is not present'


arr = list(map(int, input().split()))
n = int(input())

print(linear(arr, n))
print(binary(arr, n))