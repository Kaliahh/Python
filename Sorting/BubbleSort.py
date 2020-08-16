from random import randrange

import time

def Sort(list):
	n = len(list)
	i = 0

	while i < n:
		j = 0

		while j < (n - i - 1):
			if list[j] > list[j + 1]:
				swap(list, j, j + 1)

			j += 1

		i += 1

	return list

def swap(array, a, b):
	temp = array[a]
	array[a] = array[b]
	array[b] = temp

def create_random_list(n, x):
	list = []
	i = 0

	while i < n:
		list.append(randrange(x))
		i += 1

	return list

list = create_random_list(1000, 100)

print("Sorting...")

start = time.process_time_ns()

Sort(list)

end = time.process_time_ns()

print("Done!")

result = end - start

print(str(result) + " ns, or " + str((result) / 1000000000) + " seconds")
