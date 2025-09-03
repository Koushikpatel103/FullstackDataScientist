s = input("Enter a string: ").lower()

vowels = 0
for ch in s:
    if ch in "aeiou":
        vowels += 1

words = len(s.split())
characters = len(s.replace(" ", ""))

print("Characters:", characters)
print("Words:", words)
print("Vowels:", vowels)
