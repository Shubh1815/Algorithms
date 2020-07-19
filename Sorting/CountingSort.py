def countingSort(arr, n):

	l = max(arr) + 1
	count = [0] * l
	ans = [0] * n
	for i in arr:
		count[i] += 1 

	s = 0
	for i in range(l):
		count[i] += s 
		s = count[i]

	for i in arr:
		index = count[i] - 1
		ans[index] = i 
		count[i] -= 1
	return ans

n = int(input())
arr = list(map(int, input().split()))
print(*countingSort(arr, n))