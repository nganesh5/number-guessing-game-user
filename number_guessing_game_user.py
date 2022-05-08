import random

def numberguess(low,high):
    random_number = random.randint(low,high)
    guess = 0
    trialcount = 1
    
    while(guess != random_number):
        guess = int(input(f"Enter a number between {low} and {high}: "))
        if guess < random_number:
            print("Too low. Guess higher!")
        elif guess > random_number:
            print("Too high. Guess lower!")
        trialcount += 1
    print(f"Congrats! You have guessed the number correctly as {random_number} in {trialcount} guesses")
    
print("This game generates a random number between a set range and allow the user to guess it")    
low = int(input("Enter the min value of range: "))
high = int(input("Enter the max value of range: "))
numberguess(low, high)