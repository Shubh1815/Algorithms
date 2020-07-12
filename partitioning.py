n = int(input())
arr = list(map(int, input()))

if sum(arr) % 3 == 0:
	s = sum(arr) // 3
	dp = [[0 for i in range(n + 1)] for j in range(n + 1)]

	for i in range(1, n + 1):
		for j in range(i + 1, n + 1):
			index = 

else:
	print(0)