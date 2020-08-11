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
print(greedy_knapsack(wp, cap))