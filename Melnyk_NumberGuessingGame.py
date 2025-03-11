import random

def select_difficulty(diff):
    if diff == 1:
        print("Great! You have selected the Easy difficulty level")
        guesses = 10
    elif diff == 2:
        print("Great! You have selected the Medium difficulty level")
        guesses = 5
    elif diff == 3:
        print("Great! You have selected the Hard difficulty level")
        guesses = 3
    else:
        print("Please enter 1, 2, or 3")
    print("Let's start the game!")
    startgame(guesses)

def get_random_num():
    ans = random.randint(1, 100)
    return ans

def startgame(guesses):
    ans = random.randint(1, 100)
    originalguesses = guesses
    
    while guesses != 0:
        guesses -= 1
        userguess = int(input("Enter your guess: "))
        if userguess == ans:
            print("Congrats! You have guessed correctly!")
            print("It took you " + str(originalguesses - guesses) + " guesses to answer!")
            break
        elif userguess > ans:
            print("Incorrect! The number is less than " + str(userguess))
        elif userguess < ans:
            print("Incorrect! The number is greater than " + str(userguess))
        elif guesses == 0:
            print("GAME OVER! Sorry, you were not able to guess correctly.")
        else:
            print("Try again!")
            continue
        

### MAIN ###
playagain = "Y"
while playagain == "Y":
    print("Welcome to the number guessing game!")
    print("Try to guess the random number from 1-100!.")
    print("Please select diffiulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    diff = int(input("Enter your choice: "))
    select_difficulty(diff)
    playagain = input("Do you want to play again? (Y/N): ")






