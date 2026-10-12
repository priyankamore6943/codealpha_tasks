import random

words = ["python", "computer", "program", "coding", "developer"]

secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("=" * 35)
print("       WELCOME TO HANGMAN GAME")
print("=" * 35)

print("Guess the word one letter at a time!")
print("You have", max_attempts, "wrong guesses allowed.")

while wrong_guesses < max_attempts:

    # Display guessed word
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_attempts)

    # Check if the word is completely guessed
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        print("YOU WIN!")
        break


    guess = input("Guess a letter: ").lower().strip()


    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet!")
        continue

    # Check duplicate guesses
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
    print("\nGAME OVER!")
    print("The correct word was:", secret_word)

print("\nThank you for playing!")
























































