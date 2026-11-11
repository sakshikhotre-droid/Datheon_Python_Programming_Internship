
import random

# List of words
words = ["python", "computer", "programming",
         "college", "internship", "developer"]

# Hangman game function
def play_game():

    secret_word = random.choice(words)
    guessed_letters = []
    attempts = 6

    print("\n===== WELCOME TO HANGMAN GAME =====")

    while attempts > 0:

        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("\nWord:", display_word)
        print("Attempts left:", attempts)

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You Win!")
            return

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct Guess!")
        else:
            print("Wrong Guess!")
            attempts -= 1

    print("\nGame Over!")
    print("The correct word was:", secret_word)


# Main program
def main():
    while True:
        play_game()

        choice = input("\nPlay again? (yes/no): ").lower()

        if choice != "yes":
            print("Thank you for playing!")
            break


if __name__ == "__main__":
    main()
