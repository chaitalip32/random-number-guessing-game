import random

MAX_ATTEMPTS=7
MIN_NUMBER=1
MAX_NUMBER=100

def check_guess(guess,number):
    if guess==number:
        return "correct"
    elif guess<number:
        return "low"
    else:
        return "high"
# Rules
def display_rules():
    print("Welcome to Random Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it.\n")

def start_game(number):
    attempt = 1

    while attempt<=MAX_ATTEMPTS:
        user_input=input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter your guess: ")

        try:
            guess=int(user_input)
        except ValueError:
            print("Please enter a valid whole number.\n")
            continue

        if not MIN_NUMBER<=guess<=MAX_NUMBER:
            print(
                f"Please enter a number between "
                f"{MIN_NUMBER} and {MAX_NUMBER}.\n"
            )
            continue

        result=check_guess(guess,number)

        if result=="correct":
            print("\nCongratulations! You guessed the correct number!")
            print(f"You guessed it in {attempt} attempt(s).")
            return True
    
        if result=="low":
            print("Too low! Try a higher number.\n")
        else:
            print("Too high! Try a lower number.\n")
        
        attempt+=1
    
    print("\nGame Over!")
    print("The correct number was", number)
    return False

def main():
    """Start the guessing game."""
    display_rules()
    random_number=random.randint(MIN_NUMBER,MAX_NUMBER)
    start_game(random_number)

if __name__=="__main__":
    main()