import random

def guess_the_number():
    number = random.randint(1, 20)
    name = str(input("Hello! What is your name?\n"))

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0
    while guesses_taken < 4:
        guess = int(input("Take a guess.\n"))
        guesses_taken += 1

        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break

    if guess == number:
        print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
    elif guesses_taken == 4:
        print(f"Nope. The number I was thinking of was {number}.")
        
guess_the_number()