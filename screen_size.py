screen = (1920, 1080)

print("Width:", screen[0])
print("Height:", screen[1])

width, height = screen

total_nr_of_px = width * height

print("Pixelels: %d" % total_nr_of_px)

aspect_ratio = width / height

print("Aspect ratio: %.2f" % aspect_ratio)

portrait = (screen[1], screen[0])

print("Portrait:", portrait)

#screen[0] cannot be changed because it's a tuple and tuples are immutable
