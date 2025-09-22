import random

def hangman():
    
    words = ["python", "programming","pychamp","anaconda","HTML"]
    word = random.choice(words)  
    guessed = ["_"] * len(word)  
    attempts = 6  
    guessed_letters = []

    print(" Welcome to Hangman!")
    print(f"You have {attempts} attempts.\n")

    while attempts > 0 and "_" in guessed:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(" Please enter a single alphabet letter.\n")
            continue

        if guess in guessed_letters:
            print(" You already guessed that letter!\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f" Correct! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            attempts -= 1
            print(f" Wrong! '{guess}' is not in the word.")

        print(f"Attempts left: {attempts}\n")

    if "_" not in guessed:
        print(" Congratulations! You guessed the word:", "".join(guessed))
    else:
        print(" Game Over! The word was:", word)


# Run the game
hangman()
