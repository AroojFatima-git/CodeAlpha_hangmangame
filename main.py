import random


def choose_word():
    words = [
        "python",
        "computer",
        "programming",
        "developer",
        "keyboard"
    ]

    return random.choice(words)


def display_word(word, guessed_letters):
    result = ""

    for letter in word:
        if letter in guessed_letters:
            result += letter + " "
        else:
            result += "_ "

    return result


def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("=" * 40)
    print("         HANGMAN GAME")
    print("=" * 40)

    while attempts > 0:

        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)

        guess = input("Enter a letter: ").lower().strip()

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter exactly one letter.")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(" Correct guess!")

        else:
            attempts -= 1
            print(" Wrong guess!")

        # Check win
        if all(letter in guessed_letters for letter in word):
            print("\n YOU WIN!")
            print("The word was:", word)
            return

    print("\n GAME OVER!")
    print("The correct word was:", word)


def main():
    play_game()


if __name__ == "__main__":
    main()
