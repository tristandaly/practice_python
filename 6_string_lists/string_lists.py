letter_bucket = []

letters = input("Word: ")

for letter in letters:
    letter_bucket.append(letter)

if list(letter_bucket) == list(reversed(letter_bucket)):
    print("Palindrome!")
else:
    print("Boring old word!")
