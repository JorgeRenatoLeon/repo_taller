for x in range(1,100):
	if x%3==1 and x%5==1:
		print('FizzBuzz')
	if x%5==1:
		print('Buzz')
	if x%3==1:
		print('Fizz')
	else:
		print(x)