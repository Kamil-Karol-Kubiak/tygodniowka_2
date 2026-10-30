whole = 7
fraction = 3.75
text_number = "25"
text_decimal = "2.5"
empty = ""

print(whole, type(whole))
print(fraction, type(fraction))
print(text_number, type(text_number))
print(text_decimal, type(text_decimal))
print(empty, type(empty))

print(int(fraction), type(int(fraction)))

print(float(whole), type(float(whole)))

print(int(text_number))

print(float(text_decimal))

print(str(whole))

print(bool(0))
print(bool(1))
print(bool(empty))

print(int(True))
print(float(False))

#int(text_decimal) You cannot pass a string with a deciml point to the int() function
#because it only accepts representations of whole numbers

print(int(fraction))
print(round(fraction))
#round gives an int closest to the given float round(9.99) = 10
#int gives just an int without rounding it - int(9.99) = 9
