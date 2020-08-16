memo = {}

print("Input number")

number = int(input())

def Factorial(num):
	if num in memo:
		return memo[num]

	elif num == 1:
		return 1

	else:
		x = num * Factorial(num - 1)
		memo[num] = x
		return x

print(Factorial(number))
