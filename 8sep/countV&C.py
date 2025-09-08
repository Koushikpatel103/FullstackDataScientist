string = input("Enter a String: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0

for char in string:
    if char.isalpha():  # Only count letters
        if char in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)
