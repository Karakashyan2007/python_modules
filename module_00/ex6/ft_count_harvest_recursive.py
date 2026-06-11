def ft_count_harvest_recursive():
	day = int(input("Days untill harvest: "))
	start_day = 1
	def helper_rec(current):
		if current > day:
			print("Harvest time!")
			return
		print("Day", current)
		helper_rec(current + 1)
	helper_rec(start_day)
	