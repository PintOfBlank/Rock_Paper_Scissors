import random

pos_input = ["Rock", "Paper", "Scissors"]

rock = (pos_input[0])
paper = (pos_input[1])
scissors = (pos_input[2])

print("\nHello, welcome to my version of rock paper scissors this took a while I guess\n")

while True:
    while True:
        choice_1 = input("Choose Rock, Paper or Scissors?:\n\n")
        computer_choice = random.choice(pos_input)
        if choice_1 == "rock":
            if computer_choice == scissors:
                print("VS.")
                print(computer_choice)
                print("\nYou Broke His Scissors! (You Won!)")
                break
            elif computer_choice == paper:
                print("VS.")
                print(computer_choice)
                print("\nHe Wrapped Your Rock In His Paper! (You Lost!)")
                break
            elif computer_choice == scissors:
                print("VS.")
                print(computer_choice)
                print("\nTie")
                break
        elif choice_1 == "paper":
            if computer_choice == rock:
                print("VS.")
                print(computer_choice)
                print("\nYou Wrapped His Rock In Your Paper! (You Won!)")
                break
            elif computer_choice == scissors:
                print("VS.")
                print(computer_choice)
                print("\nHe Cut Your Paper  Up! (You Lost!)")
                break
            elif computer_choice == scissors:
                print("VS.")
                print(computer_choice)
                print("\nTie")
                break
        elif choice_1 == "scissors":
            if computer_choice == paper:
                print("VS.")
                print(computer_choice)
                print("\nYou Cut His Paper Up! (You Won!)")
                break
            elif computer_choice == rock:
                print("VS.")
                print(computer_choice)
                print("\nHis Rock Broke Your Scissors! (You Lost!)")
                break
            elif computer_choice == scissors:
                print("VS.")
                print(computer_choice)
                print("\nTie")
                break
        elif choice_1 == "q":
            quit("\nThanks For Playing :3")
        else:
            print("\nTry Again\n")


    counter = counter - 1
    play_again = input("Wanna Play Again?\n\n(Yes Or No?):\n\n")
    if play_again == "Yes" or play_again == "yes" or play_again == "y":
        print("\nLets Go Again!\n")
    elif play_again == "No" or play_again == "no" or play_again == "n":
        break

