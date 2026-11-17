# python game.py
import random


def get_value():
    return int(input("Level: "))


user_num = 0

while True:
    try:
        user_num = get_value()
        if user_num > 100 or user_num < 0:
            continue
        break

    except ValueError:
        continue


while True:
    try:
        user_guss = int(input("Guess: "))
        if user_num > 100 or user_num < 0:
            continue
        number = 0
        number = random.randint(1, user_num)

        if number == user_guss:
            print("Just right!")
            break
        elif number > user_guss and user_guss > 0:
            print("Too small!")
            continue
        elif number < user_guss and user_guss < 100:
            print("Too large!")
            continue

    except ValueError:
        continue
