# O(n) space and time complexity
def factorial(n):
	if n == 0:
		return 1 
	return n * factorial(n - 1)

n = int(input())

print(f'Recursive: {factorial(n)}')

# O(n) time complexity and O(1) space complexity
ans = 1
while n > 1:
	ans *= n
	n -= 1

print(f'Iterative: {ans}')