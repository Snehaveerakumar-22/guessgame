import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number {target_number} in {attempts} attempts.")
            break
        elif user_guess < target_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Call the number_guessing_game function
number_guessing_game()