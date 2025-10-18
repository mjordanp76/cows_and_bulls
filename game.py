"""
Cows & Bulls: A game of deductive guessing

Version 4.0 Info
- this version gives the user the option to change the length of the secret number
- this version allows secret number and user guess to have repeated digits
- adds difficulty setting options
- no input validation; no exception handling
"""

import random

# display game intro/rules
with open('rules.txt', 'r') as f:
    intro = f.read()
print(intro)

print("OPTIONS")
sec_num_size = int(input("How many digits (4-7) do you want the secret number to be?"))
diff = input("Difficulty (enter a number):\n1) unlimited tries\n2) 50 tries\n3) 10 tries")

# global variables
sec_num = []            # saved in a list so digits can be compared via indices
guess_count = 1

# set total tries according to user's chosen difficulty setting
match diff:
    case "1":
        tot_tries = 999_999
    case "2":
        tot_tries = 50
    case "3":
        tot_tries = 10

# set secret number
for n in range(sec_num_size):
    sec_num.append(random.randint(0,9))

# for testing purposes; remove before playing for real
print(sec_num)

# game loop
while guess_count <= tot_tries:
    # cow, bull, and user_num variables set inside the loop since they need to be reset after each round
    cows = 0
    bulls = 0
    user_num = []
    sec_count = {}
    user_count = {}

    guess = input("Guess the secret number: ")
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
        print(f"Remaining tries: {tot_tries - guess_count}")
        user_num.clear()
        guess_count += 1

if guess_count == 1:
    print(f"You guessed the secret number in {guess_count} try! Congratulations!")
elif guess_count > tot_tries:
    print("Sorry, you ran out of guesses.")
else:
    print(f"You guessed the secret number in {guess_count} tries! Congratulations!")
