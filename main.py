import random

def first ():
	num_sum = 0

	for x in range(1000):
		if x % 3 == 0 or x % 5 == 0 :
			num_sum += x

	print(num_sum)

def second ():
	num_sum = 0
	num_array = [1, 1]

	for x in range(4 * 10 ** 6):
		a = x % 2
		num_array[a] = sum(num_array)

		if num_array[a] % 2 == 0:
			num_sum += num_array[a]

		if num_sum > 4 * 10 ** 6:
			break

	print(num_sum)

def third ():
	num = 600851475143
	
def fourth ():
	pass


def main():
	#first()
	#second()
	third()

if __name__ == '__main__':
	main()