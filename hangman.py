import random

# List of words
words = ["apple", "python", "computer", "game", "coding"]

# Random word selection
word = random.choice(words)

# Empty list for guessed letters
guessed_letters = []

# Wrong guess counter
wrong_guesses = 0
max_wrong = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while wrong_guesses < max_wrong:

    # Display word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    # User input
    guess = input("Enter a letter: ").lower()

    # Check guess
    if guess in word:
        print("✅ Correct Guess!")
        guessed_letters.append(guess)
    else:
        print("❌ Wrong Guess!")
        wrong_guesses += 1
        print("Remaining Chances:", max_wrong - wrong_guesses)

# Lose condition
if wrong_guesses == max_wrong:
    print("\n💀 Game Over!")
    print("The correct word was:", word)
