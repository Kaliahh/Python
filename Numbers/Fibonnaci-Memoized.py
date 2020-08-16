print("How many?")

number = int(input())

memo = {}

def Fib(num):

	if num in memo:
		return memo[num]

	elif num == 0 or num == 1:
		return num

	else:
		x = Fib(num - 1) + Fib(num - 2)
		memo[num] = x
		return x


def main():
	i = 0

	while i < number:
		print(Fib(i), end = ' ')
		i += 1

main()

print()
