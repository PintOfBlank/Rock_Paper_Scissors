import random

input_choices = ["Rock", "Paper", "Scissors"]

Rock = (input_choices[0])
Paper = (input_choices[1])
Scissors = (input_choices[2])

while True:
    print("\nHello, welcome to my version of rock paper scissors this took a while I guess\n")
    choice_1 = input("Choose Rock, Paper or Scissors?\n(Write First Letter In Caps.):\n\n")
    print("VS.")
    computer_choice = random.choice(input_choices)
    print(computer_choice)

    if choice_1 == computer_choice:
        print("\nTie!")
    if choice_1 == Rock:
        if computer_choice == Scissors:
            print("\nYou Broke His Scissors! (You Won!)")
        elif computer_choice == Paper:
            print("\nHe Wrapped Your Rock In His Paper! (You Lost!)")
    elif choice_1 == Paper:
        if computer_choice == Rock:
            print("\nYou Wrapped His Rock In Your Paper! (You Won!)")
    elif computer_choice == Scissors:
        print("\nHe Cut Your Paper  Up! (You Lost!)")
    elif choice_1 == Scissors:
        if computer_choice == Paper:
            print("\nYou Cut His Paper Up! (You Won!)")
    elif computer_choice == Rock:
        print("\nHis Rock Broke Your Scissors! (You Lost!)")

    play_again = input("Wanna Play Again?\n\n(Yes Or No?):\n\n")

    if play_again == "Yes\n" or play_again == "yes\n" or play_again == "y\n":
        print("Lets Go Again!")
    elif play_again == "No\n" or play_again == "no\n" or play_again == "n\n":
        break
