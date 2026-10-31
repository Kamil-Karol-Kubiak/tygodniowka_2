sentence = input("Enter a sentence: ")
print("Characters: %d" % len(sentence))

words = sentence.split()
print("Words: %d" % len(words))

vowels = ("a", "e", "i", "o", "u")
number_of_vowels = 0
for letter in sentence.lower():
    if letter in vowels:
        number_of_vowels += 1
print("Vowels: %d" % number_of_vowels)

print("First word: %s" % words[0])

print("Last word: %s" % words[-1])

print("Reversed: %s" % sentence[::-1])

print("Words in reverse order: %s" % " ".join(words[::-1]))
