
def sum_numbers(list_of_numbers):
	total = 0;
	for num in list_of_numbers:
		total += num;	
	return total


def multiply_numbers(x,y):
	return (x*y)

if __name__ == '__main__':
	print sum_numbers([1,2,3,4])
	print multiply_numbers([1,2,3,4])
	