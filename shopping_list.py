list = []
product = 0
while product != "done":
    product = input("Enter a product (or 'done'): ")
    if product in list:
        print("%s is already on the list." % product)
    elif product == "":
        print("You added nothing.")
    elif product == "done":
        print("Thank you!\n")
    else:
        list.append(product)


remove = input("Which product should be removed (none if none)? ")
if remove == "none":
    print("Okay, list stays as it is now.")
elif remove not in list:
    print("%s is not on the list. Removed nothing." % remove)
else:
    list.remove(remove)
    print("%s has been removed" % remove)
print()
list.sort()

print("Shopping list:")
number_of_products = 0
for element in list:
    number_of_products += 1
    print("%d. %s" % (number_of_products, element))

print()
print("Number of products: %d\n" % number_of_products)
