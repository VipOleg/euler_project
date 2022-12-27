def prime_number_check (num) :
	x = 2
	while x < num / 2 :  # цикл який перевіряє всі ділимість числа на всі числа менші за перше число видає True коли число просте False коли ні
		if num % x == 0 :
			return False
		x += 1
	return True

def main ():
	pass

if __name__ == '__main__':
	main()