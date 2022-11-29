import random
def guess(x):
    Random_Number = random.randint(1,x)
    guess = 0
    while guess != Random_Number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        if guess < Random_Number:
            print("Sorry, guess again, TOO LOW!")
        elif guess > Random_Number:
            print("Sorry, guess again, TOO HIGH!")
    else:
        print(f"YOU HAVE GUESSED THE NUMBER {Random_Number} CORRECTLY!")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess =low
        feedback = input(f'is {guess} too high(h), too low(l), or correct? (c)').lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess +1
    print(f"YEY the computer guessed your number, {guess} ,correctly")

computer_guess(5)
 
computer_guess(10)
