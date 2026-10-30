product_name = input("Product: ")
unit_price = input("Price: ")
quantity = input("Quantity: ")

print("price before conversion:", type(unit_price))
print("quantity before conversion:", type(quantity))

unit_price = float(unit_price)
quantity = int(quantity)

print("price after conversion:", type(unit_price))
print("quantity after conversion:", type(quantity))
total = unit_price * quantity

print("Total: %.2f" % total)

discount_total = total * 0.9

print("Price with 10%% discount: %.2f" % discount_total)
