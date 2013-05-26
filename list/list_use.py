def even_square():
	even_squares = [x**2 for x in range(1,11) if x%2 == 0]
	return even_squares

def slice_list():
	to_21 = range(1,22)
	odds = to_21[0::2]
	middle_third = to_21[7:14:]
	print odds
	print middle_third
	
print even_square()