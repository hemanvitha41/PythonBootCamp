import random
from art import logo, vs
from game_data import data

print(logo)

current_score = 0
should_continue = True
#initial selection of A
compare_A = random.choice(data)
while should_continue:
    print(f"Compare A: {compare_A['name']}, a {compare_A['description']} from {compare_A['country']}")
    print(vs)
    compare_B = random.choice(data)
    #To make sure A is different from B
    while compare_B == compare_A:
        compare_B = random.choice(data)

    print(f"Compare B: {compare_B['name']}, a {compare_B['description']} from {compare_B['country']}")

    choice = input("Who has more followers? 'A' or 'B'").lower()

    if (choice == 'a' and compare_A['follower_count'] > compare_B['follower_count']) or (choice == 'b' and compare_B['follower_count'] > compare_A['follower_count']):
        current_score += 1
        print(f"You're right! Current Score: {current_score}")
        #Assign B as A to next round
        if compare_A['follower_count'] > compare_B['follower_count']:
            compare_A = compare_A
        else:
            compare_A = compare_B
    else:
        print(f"Sorry that's wrong!, Final Score: {current_score}")
        should_continue = False