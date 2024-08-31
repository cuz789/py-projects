"""
 Hangman game 

The Hangman program randomly selects a secret word from a list of secret words. The random module will provide this ability,
so line 1 in program imports it.

The Game: 
Here, a random word (a fruit name) is picked up from our collection and the player gets limited chances to win the game.
When a letter in that word is guessed correctly, that letter position in the word is made visible. In this way, all letters of the word are to be guessed before all the chances are over. 
For convenience, we have given length of word + 2 chances. For example, word to be guessed is mango, then user gets 5 + 2 = 7 chances, as mango is a five-letter word.

"""


import random

secret_words = ['Eren', 'Mikasa', 'Armin', 'Levi', 'Jean', 'Reiner', 'Hanji', 'Erwin', 'Gabi', 'Zeke', 'Connie', 'Sasha']
word = random.choice(secret_words).lower()  
word_len = len(word)
chance = word_len + 3

def hangman():
    print(f"Guess the AOT character name of length {word_len} characters")
    guessed_word = ['_'] * word_len  
    guessed_letters = set()  # To keep track of guessed letters
    attempts = chance

    while attempts > 0:
        print("\nWord: " + ' '.join(guessed_word))
        guess = input("Enter a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed that letter.")
            else:
                guessed_letters.add(guess)

                if guess in word:
                    for i in range(word_len):
                        if word[i] == guess:
                            guessed_word[i] = guess
                    print(f"Good guess! The letter '{guess}' is in the word.")
                else:
                    attempts -= 1
                    print(f"Incorrect guess! You have {attempts} attempts left.")
        else:
            print("Enter a single alphabet character.")

        if '_' not in guessed_word:
            print(f"\nCongratulations! You've guessed the word: {word.capitalize()}")
            break
    else:
        print(f"\nSorry, you've run out of attempts. The word was: {word.capitalize()}")

# Run the game
hangman()
