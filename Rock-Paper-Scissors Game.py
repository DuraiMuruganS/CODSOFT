import random
# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"
# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
# Main game function
def rock_paper_scissors_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    
    while True:
        # Get the user's choice
        user_choice = input("\nEnter your choice (rock, paper, or scissors): ").lower()
        # Validate the user's choice
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        # Get the computer's choice
        computer_choice = get_computer_choice()
        # Determine the result
        result = determine_winner(user_choice, computer_choice)
        # Display the results
        print(f"\nYour choice: {user_choice}")
        print(f"Computer's choice: {computer_choice}")
        print(result)
        # Update the score
        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1
        # Display the current score
        print(f"Score: You {user_score} - Computer {computer_score}")
        # Ask if the user wants to play again
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Final Score:")
            print(f"You: {user_score} - Computer: {computer_score}")
            break
# Run the game
rock_paper_scissors_game()
