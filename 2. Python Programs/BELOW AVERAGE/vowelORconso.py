ch = input("Enter a character: ")

if len(ch) == 1 and ch.isalpha():
    if ch.lower() in 'aeiou':
        print(f"{ch} is a vowel.")
    else:
        print(f"{ch} is a consonant.")
else:
    print("Please enter a single alphabet character.")