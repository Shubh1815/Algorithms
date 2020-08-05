def exponentiation(base, expo):
	ans = 1 
	while expo > 0:
		if expo % 2 == 1:
			ans *= base 
			expo -= 1

		base *= base
		expo //= 2 

	return ans


base, expo = map(int, input().split())

print(exponentiation(base, expo))