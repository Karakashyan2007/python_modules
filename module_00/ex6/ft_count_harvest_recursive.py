def helper_recursive(count):
	if(1 < count):
		helper_recursive(count - 1)
	print("Day", count)

def ft_count_harvest_recursive():
	day = int(input("Days until harvest: "))
	helper_recursive(day)
	print("Harvest time!")