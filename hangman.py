import random

# Words for the game
words = ["PYTHON", "COMPUTER", "HANGMAN", "PROGRAM", "LAPTOP"]

# Hangman drawings
stages = [
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """
]

def play_hangman():
    secret_word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_attempts = 6

    print("\n===== HANGMAN WORD GUESSING GAME =====")

    while wrong_guesses < max_attempts:
        print(stages[max_attempts - wrong_guesses])
        display_word = " ".join(
            letter if letter in guessed_letters else "_"
            for letter in secret_word
        )

        print("Word:", display_word)
        print("Guessed letters:", " ".join(sorted(guessed_letters)))
        print(f"Wrong attempts: {wrong_guesses}/{max_attempts}")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won!")
            return

        guess = input("Guess one letter: ").strip().upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one letter (A-Z).")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            wrong_guesses += 1
            print("Wrong guess!")

    print(stages[0])
    print("\nGame Over! You lost.")
    print("The secret word was:", secret_word)


if __name__ == "__main__":
    play_hangman()