fruits = ["apple", "banana", "cherry"]
numbers = [4, 7, 2, 9, 1]
word = "Python"

for fruit in fruits:
    print(fruit)

print()

for fruit in fruits:
    print("Word %s containes %d letters" % (fruit, len(fruit)))

print()

total = 0
for number in numbers:
    total += number
print(total)

print()

even = 0
for number in numbers:
    if number % 2 == 0:
        even += 1
print("Number of even numbers: %d" % even)

print()

for letter in word:
    print(letter)

print()

for i in range(5):
    print(i)
