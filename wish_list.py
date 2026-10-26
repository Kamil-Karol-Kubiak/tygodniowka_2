list = []

list.append(input("Enter product 1: "))
list.append(input("Enter product 2: "))
list.append(input("Enter product 3: "))
print()
print(list)


remove = (input("Which product do you want to remove? "))

if remove in list:
	list.remove(remove)
	print("%s has been removed." % remove)
else:
	print("%s was not fount." % remove)
print("Final list: ", list)
