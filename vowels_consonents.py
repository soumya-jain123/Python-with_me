my_string = str(input("Enter the string: "))

count_vowel = 0
count_consonent = 0

for x in my_string:
    if (x=='a') or (x=='e') or (x=='i') or (x=='o') or (x=='u'):
        count_vowel += 1
    else:
        count_consonent += 1

print(f"no. of vowels: {count_vowel}")
print(f"no. of consonents: {count_consonent}")