import random

print("Hello, World!")
while True:
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors) or 'quit' to exit: ").lower()

    if user_choice == 'quit':
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice.")
    else:
        print(f"Computer chose: {computer_choice}")
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("You win!")
        else:
            print("Computer wins!")
choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if user_choice not in choices:
    print("Invalid choice.")
else:
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        print("You win!")
    else:
        print("Computer wins!")