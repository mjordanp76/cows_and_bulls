"""
Cows & Bulls: A game of deductive guessing

Version 1.0 Info
- secret number is 4 digits long; no option to change that
- every digit in the secret number is unique
- unlimited tries; no options for difficulty
- no input validation; no exception handling
"""

import random

# display game intro/rules
with open('rules.txt', 'r') as f:
    intro = f.read()
print(intro)

# global variables
sec_num = random.sample(range(0,9), 4) # 4-digit secret number without repeating digits
guess_count = 1

# for testing purposes
print(sec_num)

# checks to make sure user's guess has no repeated digits
def Duplicates(num):
    for n in num:
        if num.count(n) > 1:
            return True
    return False

# game loop
while True:
    # cow, bull, and user_num variables set inside the loop since they need to be reset after each round
    cows = 0
    bulls = 0
    user_num = []
    guess = input("Guess the secret number: ")
    for digit in guess:
        user_num.append(int(digit))
    if Duplicates(user_num):
        print("Your guess cannot contain repeated digits.\nPlease guess again.")
        continue
    # compare user's guess and secret number
    if user_num == sec_num:
        break
    for n in range(4):
        if user_num[n] in sec_num:
            if user_num[n] == sec_num[n]:
                bulls += 1
            else:
                if user_num[n]:
                    cows += 1
    if bulls == 4:
        break
    else:
        print(f"Cows: {cows}\nBulls: {bulls}")
        user_num.clear()
        guess_count += 1

if guess_count == 1:
    print(f"You guessed the secret number in {guess_count} try! Congratulations!")
else:
    print(f"You guessed the secret number in {guess_count} tries! Congratulations!")
