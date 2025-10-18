"""
Cows & Bulls: A game of deductive guessing

Version 3.0 Info
- this version gives the user the option to change the length of the secret number
- this version allows secret number and user guess to have repeated digits
- unlimited tries; no options for difficulty
- no input validation; no exception handling
"""

import random

# display game intro/rules
with open('rules.txt', 'r') as f:
    intro = f.read()
print(intro)

print("OPTIONS")
sec_num_size = int(input("How many digits (4-7) do you want the secret number to be?"))

# global variables
sec_num = []            # saved in a list so digits can be compared via indices
guess_count = 1

# set secret number
for n in range(sec_num_size):
    sec_num.append(random.randint(0,9))

# for testing purposes; remove before playing for real
print(sec_num)

# game loop
while True:
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
        user_num.clear()
        guess_count += 1

if guess_count == 1:
    print(f"You guessed the secret number in {guess_count} try! Congratulations!")
else:
    print(f"You guessed the secret number in {guess_count} tries! Congratulations!")
