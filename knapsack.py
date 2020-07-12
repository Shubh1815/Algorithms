def knapsack(wp, cap):
	dp = [0 for _ in range(cap + 1)]

	for i in range(1, cap + 1):
		maxi = 0
		for w, p in wp:
			index = i - w
			if index >= 0:
				maxi = max(maxi, dp[index] + p)
		dp[i] = maxi

	print(dp)
	return dp[cap] 

def discrete_knapsack(wp, cap):
	dp = [[0 for i in range(cap + 1)] for j in range(len(wp) + 1)]
	
	for i in range(1, len(wp) + 1):
		w, p = wp[i - 1]
		for j in range(cap + 1):
			index = j - w 
			maxi = dp[i - 1][j]
			if index >= 0:
				maxi = max(maxi, dp[i - 1][index] + p)

			dp[i][j] = maxi

	return dp[len(wp)][cap]

def greedy_knapsack(wp, cap):
	for i in range(len(wp)):
		w, p = wp[i]
		wp[i] += tuple([p / w])

	wp = sorted(wp, key=lambda x: (x[2], -x[0]), reverse=True)
	profit = 0
	for w, p, r in wp:
		if cap > 0:
			curr = min(cap, w)
			profit += (r * curr)
			cap -= curr 
		else:
			break 

	return '{0:.4f}'.format(profit)

cap, n = map(int, input().split())

weights = list(map(int, input().split()))
profit = list(map(int, input().split()))

wp = list(zip(weights, profit))
print(discrete_knapsack(wp, cap))