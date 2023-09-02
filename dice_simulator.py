import random

def roll_dice():
    return random.randint(1, 6)

while True:
    input("Press Enter to roll the dice...")
    result = roll_dice()
    print(f"You rolled a {result}")

    play_again = input("Do you want to roll again? (y/n): ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break
 