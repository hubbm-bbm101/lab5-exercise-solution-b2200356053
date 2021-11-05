import random 

print("Welcome to guessing game")
number = random.randint(1,10)
guess = 0
while guess != number:
    guess = int(input("Enter a number between 1 to 10: "))
    if guess > number:
        print("Decrease your number")
    elif guess < number:
        print("Increase your number")
else:
    print(f"You won, number is {number}")