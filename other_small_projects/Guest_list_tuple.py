def guest_list(guests):
	for x in guests:
		name, age, profession = x
		print("{} is {} years old and works as {}.".format(name, age, profession))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])