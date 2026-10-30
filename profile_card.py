for x in range(2):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter a city you live in: ")
    height = float(input("Enter your height (in meters): "))

    print("===== PROFILE =====")
    print("Name: %s" % name)
    print("Age: %d" % age)
    print("City: %s" % city)
    print("Height: %.2f" % height)
    print("===================")
    x += 1
