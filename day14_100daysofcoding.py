#Breaking the problem into small block of code
from art_higherlower import logo
from higher_lowergamedata import data
from art_higherlower import vs
import random
#TODO-1 display art
print(logo)
#score count variable
score = 0

account_b = random.choice(data)
#flage for while loop
game_should_continue = True
#TODO-8 Make The game repeatedable
while game_should_continue:
    #TODO-3 Format the account data in the printable format
    def format_data(account):
        """Format the account dat in the printable format"""
        account_name = account["name"]
        account_descr = account["description"]
        account_country = account["country"]
        # print data
        return f"{account_name},a {account_descr}, from {account_country}"

    #TODO-2 Generate a random account  from the higher_lowergame data

    # TODO-9 make account at postion B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b =random.choice(data)
    print(f"Compare A:{format_data(account_a)}.")
    print(vs)
    print(f"Compare B:{format_data(account_b)}.")

    ##TODO-5.2 Use if statement to check if user is correct
    def check_answer(guess, a_followers, b_followers):
        """take the user guess and follower counts and return if they got it right"""
        if a_followers > b_followers:
            return guess == "a"
        else:
            guess == "b"

    #TODO-4 Ask the user for  guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    #TODO-5 Check if the user is correct
    ##TODO-5.1 Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # TODO-10 Clear the screen between rounds
    #clear()
    #This function will clear te screen but is't disable because it's not functional in python
    print(logo)
    #TODO-6 Gove user fedback on their game
    #TODO-7 Score Keeping
    if is_correct:
        score += 1
        print(f"You're right, Current Score {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong, Final Score {score}")





