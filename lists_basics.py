tasks = ["study", "exercise", "read", "code"]

print(tasks)

print(len(tasks))

tasks.append("review")

print(tasks)

tasks.insert(0, "plan")

print(tasks)

tasks[3] = "read a book"

print(tasks)

tasks.remove("exercise")

print(tasks)

second_list = tasks
second_list.append("test")
print()
print(tasks)
print(second_list)
