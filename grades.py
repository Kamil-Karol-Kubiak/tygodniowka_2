grades = [45, 72, 88, 51, 90, 63]

total = 0
for grade in grades:
    total += grade
print("Total: %d" % total)


avg = 0
for grade in grades:
    avg += grade / len(grades)
print("Average: %.2f" % avg)


passing_grades = 0
for grade in grades:
    if grade >= 50:
        passing_grades += 1
print("Passing grades: %d" % passing_grades)


max = 0
for grade in grades:
    if grade > max:
        max = grade
print("Highest: %d" % max)


min = 100

for grade in grades:
    if grade < min:
        min = grade
print("Lowest: %d" % min)
