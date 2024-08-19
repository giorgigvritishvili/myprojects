import random

def guessing_game():
    # Display a welcome message
    print("Welcome to the Guess game")
    print("მე ვფიქრონ რიცხვი 1 და 100 შუა.")

   
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
         
            player_guess = int(input("Enter your guess: "))
            
           
            attempts += 1
            
          
            if player_guess < number_to_guess:
                print("Too low! Try again.")
            elif player_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    guessing_game()

