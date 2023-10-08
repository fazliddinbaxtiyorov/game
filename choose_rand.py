import random
import time


def choose():
    while True:
        print('Welcome to Random Game \n'
              'Enter random number \n')
        enter = input('Enter random number 1 to 10: ')
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        res = random.choice(enter)
        chooses = random.choice(number)
        if res == int(enter):
            time.sleep(1)
            print(res)
            time.sleep(0.5)
            print(chooses)
            time.sleep(0.4)
            print("Congratulation you win 🎉")
        else:
            time.sleep(1)
            print(res)
            time.sleep(0.5)
            print(chooses)
            time.sleep(0.4)
            print("Sorry you lose 🥲")
            time.sleep(0.6)
            print("Please, repeat one more")


