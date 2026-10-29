sentence = input("Write a sentence: ")

print("First five characters: %s" % sentence[:5])
print("Last five characters: %s" % sentence[-5:])
print("Every cecond character: %s" % sentence[::2])
print("Reversed: %s" % sentence[::-1])
print("Withount first and last character: %s" %sentence[1:-1])

length = len(sentence)

if length % 2 == 1:
	print("Middle letter: %s" % sentence[length // 2])
else:
	print("Middle letters: %s" % sentence[length // 2 - 1] + sentence[length // 2])
