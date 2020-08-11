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

cap, n = map(int, input().split())

weights = list(map(int, input().split()))
profit = list(map(int, input().split()))

wp = list(zip(weights, profit))
print(discrete_knapsack(wp, cap))