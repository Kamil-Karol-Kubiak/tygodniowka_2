days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
temperatures = (18, 21, 19, 24, 22, 17, 20)

for i in range(len(days)):
    print("%s: %d°C" % (days[i], temperatures[i]))

average = 0
for temperature in temperatures:
    average += float(temperature)
average = average / len(temperatures)
print("Average temperature: %.2f°C" % average)

highest = temperatures[0]
highest_days = days[0]
for i in range(len(temperatures)):
    if temperatures[i] > highest:
        highest = temperatures[i]
        highest_days = days[i]
print("Highest: %d°C on %s" % (highest, highest_days))

lowest = temperatures[0]
lowest_days = days[0]
for i in range(len(temperatures)):
    if temperatures[i] < lowest:
        lowest = temperatures[i]
        lowest_days = days[i]
print("Lowest: %d°C on %s" % (lowest, lowest_days))

days_above_avg = 0
for temperature in temperatures:
    if temperature > average:
        days_above_avg += 1
print("Days above average: %d" % days_above_avg)
