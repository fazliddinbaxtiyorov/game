from quiz import quiz
from choose_rand import choose


def start():
    print('Welcome to The Game \n'
          'You can play Two game Quiz and Random\n'
          'Choose the Game: Quiz or Random')
    enter = input('Enter: ')

    if enter.lower() == 'quiz':
        quiz()
    elif enter.lower() == 'random':
        choose()
    else:
        print(f"We don't have the {enter} game")


start()
