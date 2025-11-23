import random

def number_guessing_game():
    """
    A simple number guessing game where the user tries to guess a random number
    between 1 and 100.
    """
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts to guess it.")
    
    while attempts < max_attempts:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check if the guess is correct
            if guess == number_to_guess:
                print(f"Congratulations! You guessed the number in {attempts} attempts!")
                return
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
                
            # Show remaining attempts
            remaining_attempts = max_attempts - attempts
            if remaining_attempts > 0:
                print(f"You have {remaining_attempts} attempts left.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    play_again = "yes"
    while play_again.lower() == "yes":
        number_guessing_game()
        play_again = input("Do you want to play again? (yes/no): ")
    print("Thanks for playing!") 
    
    
