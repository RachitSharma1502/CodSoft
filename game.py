import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_points = 0
    computer_points = 0
    round_number = 1

    print("===== Welcome to Sharmaji's Rock-Paper-Scissors Game! =====")

    while True:
        print(f"\n🔄 Round {round_number} - Choose rock, paper, or scissors (or 'quit' to exit):")
        user_choice = input("Your choice: ").lower().strip()

        if user_choice == 'quit':
            print("\nThanks for playing with Sharmaji! Final Scores:")
            print(f"You: {user_points} | Computer: {computer_points}")
            print("💙 Have a great day! Bye ")
            break
        elif user_choice not in ['rock', 'paper', 'scissors']:
            print("⚠ Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f" Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)
        print(result)

        if "win" in result:
            user_points += 1
        elif "lose" in result:
            computer_points += 1

        print(f"📊 Scoreboard -> You: {user_points} | Computer: {computer_points}")

        play_again = input("Play another round? (y/n): ").lower().strip()
        if play_again != 'y':
            print("\n Thanks for playing with Sharmaji! Final Scores:")
            print(f" You: {user_points} |  Computer: {computer_points}")
            print(" Keep rocking! Bye ")
            break

        round_number += 1

if __name__ == "__main__":
    play_game()
