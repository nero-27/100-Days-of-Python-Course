from game_data import data
from art import logo, vs
import random
from replit import clear

print(logo)
data_len = len(data)
# pick 2 random data to compare
a, b = random.randint(0, data_len - 1), random.randint(0, data_len - 1)

pickA, pickB = data[a], data[b]
user_wins = True
user_score = 0
# in a while loop, ask user to choose from pick
while user_wins == True:
    clear()
    print(logo)
    print(
        f"Compare A: {pickA['name'], pickA['description']} from {pickA['country']}"
    )
    print(vs)
    print(
        f"Compare B: {pickB['name'], pickB['description']} from {pickB['country']}"
    )

    hm = {'A': pickA, 'B': pickB}
    user_pick = input("Which has higher followers? A or B : ")
    user_pick = hm[user_pick]
    followerA = pickA['follower_count']
    followerB = pickB['follower_count']

    if user_pick['follower_count'] == max(followerA, followerB):
        user_score += 1
        pickA = user_pick
    else:
        user_wins = False
        print(f"You're wrong. Score : {user_score}")
        break

    pickB = data[random.randint(0, data_len - 1)]

# maintain user score
# if user is right, take winner and pick another random from data
# continue while till user is wrong
