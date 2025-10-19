"""
Cows & Bulls: A game of deductive guessing

Version 5.0 Info
- this version gives the user the option to change the length of the secret number
- this version allows secret number and user guess to have repeated digits
- this version adds difficulty setting options
- this version includes input validation and exception handling
- this version allows user to play again
"""

import random

# display game intro/rules
try:
    with open("rules.txt", "r") as f:
        intro = f.read()
except FileNotFoundError:
    intro = ("Welcome to the Cows & Bulls Game.\n"
            "Try to guess the secret number.\n"
            "If your guess contains a correct digit in the correct spot, you'll get a bull.\n"
            "If you guess contains a correct digit, but in the wrong spot, you'll get a cow.\n")
print(intro)

# outer game loop
play_again = 'y'

while play_again.lower() == 'y':
    print("OPTIONS")
    # get secret number length from user
    while True:
        try:
            sec_num_size = int(input("How many digits (4-7) do you want the secret number to be?"))
            if 4 <= sec_num_size <= 7:
                break
            else:
                print("Please enter a number between 4 and 7")
        except ValueError:
            print("That's not a number. Please enter a number between 4 and 7")

    # get difficulty setting from user
    while True:
        try:
            diff = input("Difficulty (enter a number):\n1) unlimited tries\n2) 50 tries\n3) 10 tries")
            if 1 <= int(diff) <= 3:
                break
            else:
                print("Please enter a number between 1 and 3")
        except ValueError:
            print("That is not one of the choices. Please enter a number between 1 and 3")

    # global variables
    sec_num = []            # saved in a list so digits can be compared via indices
    guess_count = 1

    # set total tries according to user's chosen difficulty setting
    match diff:
        case "1":
            tot_tries = float("inf")
        case "2":
            tot_tries = 50
        case "3":
            tot_tries = 10

    # set secret number
    for n in range(sec_num_size):
        sec_num.append(random.randint(0,9))

    ### FOR TESTING PURPOSES; REMOVE BEFORE PLAYING FOR REAL
    print(sec_num)

    ### MAIN GAME LOOP
    while guess_count <= tot_tries:
        # cow, bull, and user_num variables set inside the loop since they need to be reset after each round
        cows = 0
        bulls = 0
        user_num = []
        sec_count = {}
        user_count = {}

        while True:
            guess = input("Guess the secret number: ")
            if not guess.isdigit():
                print("Your guess cannot contain non-numerical characters. Guess again.")
            elif len(guess) != sec_num_size:
                print("Your guess is too long/short. Guess again.")
            else:
                break
        for digit in guess:
            user_num.append(int(digit))

        # compare user's guess and secret number
        if user_num == sec_num:
            break
        for n in range(sec_num_size): # count bulls
            if user_num[n] == sec_num[n]:
                bulls += 1
            else: # keep track of non-bulls
                sec_count[sec_num[n]] = sec_count.get(sec_num[n], 0) + 1
                user_count[user_num[n]] = user_count.get(user_num[n], 0) + 1
        for i in user_count: # count cows
            if i in sec_count:
                cows += min(sec_count[i], user_count[i])
                '''This prevents digits that appear more in user guess than in secret number from
                causing too many cows to be counted.
                '''

        else:
            print(f"Cows: {cows}\nBulls: {bulls}")
            if diff == "1":
                print("Remaining tries: Infinite")
            else:
                print(f"Remaining tries: {tot_tries - guess_count}")
            user_num.clear()
            guess_count += 1

    if guess_count == 1:
        print(f"You guessed the secret number in {guess_count} try! Congratulations!")
    elif guess_count > tot_tries:
        print("Sorry, you ran out of guesses.")
    else:
        print(f"You guessed the secret number in {guess_count} tries! Congratulations!")

    while True:
        play_again = input("Would you like to play again? y/n: ")
        if play_again.lower() == 'y' or play_again.lower() == 'n':
            break
        else:
            continue

print("\nThank you for playing Cows & Bulls! See you next time!")