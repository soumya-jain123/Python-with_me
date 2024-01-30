import random

def display_choices():
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

def get_useer_choice():
    display_choices()
    choice = int(input("Enter your choice please(1 or 2 or 3):"))
    return choice

def get_computer_choice():
    choices = [1,2,3]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    print("\nYour choice:")
    display_choice_image(user_choice)
    print("\ncomputer's choice:")
    display_choice_image(computer_choice)

    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 1 and computer_choice == 3) or
        (user_choice == 2 and computer_choice == 1) or
        (user_choice == 3 and computer_choice == 2)
    ):
        return "You win!"
    else:
        return "Computer wins!"
    
def display_choice_image(choice):
    if choice == 1:
        print("   _______")
        print("--'   ____)")
        print("      (_____)")
        print("      (_____)")
        print("      (____)")
        print("---.__(___)")
    elif choice == 2:
        print("    _______")
        print("--'   ____)____")
        print("          ______)")
        print("          _______)")
        print("         _______)")
        print("---.__________)")
    elif choice == 3:
        print("    _______")
        print("--'   ____)____")
        print("          ______)")
        print("       __________)")
        print("      (____)")
        print("---.__(___)")

def main():
    user_choice = get_useer_choice()
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)
    print(result)

main()