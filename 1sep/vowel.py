a = input("Enter a string: ")
vcount = 0
ccount = 0

for ch in a.lower():   # make lowercase for simplicity
    if ch in "aeiou":
        vcount += 1
    else:
        ccount += 1

print("Vowels:", vcount)
print("Consonants:", ccount)
