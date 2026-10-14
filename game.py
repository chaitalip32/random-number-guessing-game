import random

attempts=7

# Rules
def display_rules():
    print("Welcome to Random Number Guessing Game!\n")
    print("I have selected a number between 1 and 100.")
    print(f"You have {attempts} attempts to guess it.\n")

def start_game(number,attempt=1):
    if attempt>attempts:
        print("\nGame Over!")
        print("The correct number was",number)
        return

    guess=input(f"Attempt {attempt}/{attempts} - Enter your guess: ")

    try:
        guess=int(guess)
    except ValueError:
        print("Please enter a valid number.\n")
        return start_game(number, attempt)
    
    # Check number range
    if guess<1 or guess>100:
        print('Please enter the number between 1 and 100.\n')
        return start_game(number, attempt)
    
    check_result= lambda x,y : "correct" if x==y else(
        "low" if x<y else "high")

    result=check_result(guess,number)

    if(result=="correct"):
        print("\nCongratulations! You guessed the correct number!")
        print(f"You guessed it in {attempt} attempt(s).")
        return
    if result=="low":
        print("Too low! Try a higher number.\n")
    else:
        print("Too high! Try a lower number.\n")

    start_game(number, attempt+1)

display_rules()
random_number=random.randint(1,100)
start_game(random_number)