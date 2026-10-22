import random

def play_game():

    choices = ["stone", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    print("welcome to stone, paper, scissors game")
    print("rule of game is: stone beats scissors | scissors beats paper | paper beats stone")

    while True:

        user_choice = input("enter stone, paper, scissors (or 'quit' to exit)").lower()

        if user_choice == "quit":
            break
        if user_choice not in choices:
            print("Invalid choice ! please try again")
            continue

        computer_choice = random.choice(choices)

        print(f"computer choose: {computer_choice.capitalize()}")
        print(f"you choose: {user_choice.capitalize()}")

        if user_choice == computer_choice:
            print("the match is tie")

        elif(
            (user_choice =="stone" and computer_choice == "scissors")or
            (user_choice == "scissors" and computer_choice == "paper")or
            (user_choice == "paper" and computer_choice == "stone")
        ):
            print("you win this round")
            user_score += 1

        else:
            print("computer win this round")
            computer_score += 1

        print(f"score-> you: {user_score} | computer: {computer_score}")
        print("-" * 40 + "\n")

    print("\n ==the game is over==")
    print(f"Final Score -> You: {user_score} | Computer: {computer_score}")

    if user_score > computer_score:
        print("congratulations you win this match")

    elif(computer_score > user_score):
        print("computer win! better luck for next time")

    else:
        print("the overall match is tie")
    print("thanks for playing")

if __name__ == "__main__":
    play_game()

