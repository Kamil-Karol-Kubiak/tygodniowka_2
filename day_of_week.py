days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
number = int(input("Choose a number from 1 to 7: "))
if number <= 7 and number >= 1:
	print("Day: %s" % days[number - 1])
else:
	print("ERROR: number's outside the range")
