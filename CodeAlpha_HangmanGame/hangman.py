
import random

words = ["apple", "python", "computer", "school", "program"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("Welcome to Hangman!")

while wrong_guesses < max_wrong_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)

    if all(letter in guessed_letters for letter in secret_word):
        print("You win! The word was:", secret_word)
        break

    guess = input("Enter one letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("Game over! The word was:", secret_word)
