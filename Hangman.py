import random

def play_hangman():
    # 1. Setup a list of 5 predefined words
    words = ["mother", "program", "laptop", "banana", "coding"]
    
    # 2. Randomly select one word from the list
    secret_word = random.choice(words)
    
    # 3. Track game state variables
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6
    
    print("Welcome to Hangman!")
    print(f"You can make up to {max_incorrect} incorrect guesses before the game ends.")
    
    # 4. Game Loop
    while incorrect_guesses < max_incorrect:
        # Display the current hidden word state (e.g., p _ t h _ n)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        
        print("\nWord: " + display_word.strip())
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        # Check if the player has uncovered all letters
        if "_" not in display_word:
            print(f"\n🎉 Congratulations! You guessed the word: {secret_word}")
            break
            
        # Get user input
        guess = input("Guess a letter: ").lower().strip()
        
        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Invalid input. Please enter a single alphabetical letter.")
            continue
            
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try a different one.")
            continue
            
        # Record the guess
        guessed_letters.append(guess)
        
        # Process correct or incorrect guess
        if guess in secret_word:
            print(f"✅ Good job! '{guess}' is in the word.")
        else:
            print(f"❌ Oops! '{guess}' is not in the word.")
            incorrect_guesses += 1
            
    # Lose condition
    if incorrect_guesses >= max_incorrect:
        print(f"\n💀 Game Over! You've run out of guesses. The word was: {secret_word}")

# Run the game
if __name__ == "__main__":
    play_hangman()