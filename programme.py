palindrome = 0
i = 100
while i < 1000:
	j = 100
	while j < 1000:
		product = i * j
		x = str(product)
		y = str(product)
		y = y[::-1]
		if x == y and product > palindrome:
			palindrome = product

		j += 1

    	
	i += 1
	print palindrome
