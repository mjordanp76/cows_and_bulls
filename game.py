"""
Cows & Bulls: A game of deductive guessing

Version 2.0 Info
- this version gives the user the option to change the length of the secret number
- every digit in the secret number is unique
- unlimited tries; no options for difficulty
- no input validation; no exception handling
"""

import random

# display game intro/rules
with open('rules.txt', 'r') as f:
    intro = f.read()
print(intro)

print("OPTIONS")
sec_num_size = int(input("How many digits (4 -7) do you want the secret number to be?"))
# global variables
sec_num = random.sample(range(0,9), sec_num_size) # secret number without repeating digits
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
    for n in range(sec_num_size):
        if user_num[n] in sec_num:
            if user_num[n] == sec_num[n]:
                bulls += 1
            else:
                if user_num[n]:
                    cows += 1
    if bulls == sec_num_size:
        break
    else:
        print(f"Cows: {cows}\nBulls: {bulls}")
        user_num.clear()
        guess_count += 1

if guess_count == 1:
    print(f"You guessed the secret number in {guess_count} try! Congratulations!")
else:
    print(f"You guessed the secret number in {guess_count} tries! Congratulations!")
