import random

choices = ["rock", "paper", "scissors"]

rob = random.choice(choices)

print("Choose: rock, paper, or scissors")
user = input("Your choice: ").lower()

if user not in choices:
    print("Invalid choice!")
else:
    print(f"You chose {user}")
    print(f"Computer chose {rob}")

    if user == rob:
        print("It's a tie!")
    elif (user == "rock" and rob == "scissors") or \
         (user == "paper" and rob == "rock") or \
         (user == "scissors" and rob == "paper"):
        print("You won!")
    else:
        print("Computer won!")