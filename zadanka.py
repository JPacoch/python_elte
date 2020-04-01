import random

#guess a number
print("Hello! Welcome to the 'Guess a number' game! What is your name? ")
name = input()
name = str(name)
print("Hello %s" % name)
num = random.randint(1,100)

guess = str(input("Ready? "))


while guess != num:
    print("Guess a number between 1 and 100.")
    guess = input()
    guess = int(guess)

    if guess < num:
        print("The number is too low")

    if guess > num:
        print("The number is too large")

    if guess == num:
        print("Nice! You are correct!")
        break


#kamien papier nozyczki
l = ['Rock', 'Paper', 'Scissors' ]
AI = l[random.randint(0,2)]

num_of_games = 0

while num_of_games < 5:
    human = input("1, 2, 3... ")

    num_of_games = num_of_games + 1
    try:
        if human == AI:
            print("That's a draw.")
        elif human  == "Paper":
            if AI == "Rock":
                print("You won!")
            else:
                print("You lost.")
        elif human == "Rock":
            if AI == "Paper":
                print("You lost.")
            else:
                print("You won!")
        elif human == "Scissors":
            if AI == "Paper":
                print("You won!")
            else:
                print("You lost.")
    except ValueError:
        print("Pick from 'Rock', 'Paper' or 'Scissors'!")
        break

