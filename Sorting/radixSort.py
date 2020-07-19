# O(n)
def pad_zero(arr, n):
	max_digits = 0
	for i in arr:
		max_digits = max(max_digits, len(str(i)))

	for i in range(n):
		d = len(str(arr[i]))
		times = max_digits - d
		arr[i] = ('0' * times) + str(arr[i])

	return max_digits

# O(n)
def countingSort(arr, n, dpos):

	count = [0] * 10
	ans = [''] * n

	for num in arr:
		count[int(num[dpos])] += 1 

	s = 0
	for i in range(10):
		count[i] += s 
		s = count[i]

	for j in range(n - 1, -1, -1):
		num = arr[j]
		index = count[int(num[dpos])] - 1
		ans[index] = num 
		count[int(num[dpos])] -= 1

	return ans 	# all nums in array are String

# O(n * digits)
def radixSort(arr, n):
	digits = pad_zero(arr, n) # Padding num with zeros, so all digits have same length

	for i in range(digits):
		arr = countingSort(arr, n, digits - i - 1)
	
	return list(map(int, arr)) # Converting all nums in array to integer


n = int(input())
arr = list(map(int, input().split()))
print(*radixSort(arr, n))
