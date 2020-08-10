n = int(input())
change = list(map(int, input().split()))

dp = [0 for i in range(n + 1)]

for coin in change:
	for i in range(n + 1):
		if i - coin >= 0:
			if not dp[i]:
				dp[i] = dp[i - coin] + 1 
			else:
				dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[n])