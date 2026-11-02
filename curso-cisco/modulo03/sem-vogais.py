word_without_vowels = ""

user_word = input("Digite uma palavra: ")

vowels = ["A", "E", "I", "O", "U"]

for letter in user_word:
    letter = letter.upper()
    if letter not in vowels:
       word_without_vowels += letter

print(word_without_vowels)
