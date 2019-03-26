for x in range(1,100):
	if x%3==1 and x%5==1:
		print('FizzBuzz')
	else:
		if x%5==1:
			print('Buzz')
		else:
			if x%3==1:
				print('Fizz')
			else:
				print(x)