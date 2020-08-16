
print("How many?")

number = int(input())

print()

def Fib(num):
	if num == 0:
		return 0

	elif num == 1:
		return 1

	else:
		return (Fib(num - 1) + Fib(num - 2))



def main():
	i = 0

	while i < number:
		print(Fib(i), end = ' ')
		i += 1

main()

print()
