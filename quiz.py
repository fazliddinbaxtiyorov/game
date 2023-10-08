def quiz():
    print('Welcome to Python Quiz')
    answer = input('Are you ready to play the Quiz ? (yes/no) :')
    score = 0
    total_questions = 10

    if answer.lower() == 'yes':
        print('var = "James" * 2  * 3\n'
              'print(var)')
        print('a = JamesJamesJamesJamesJamesJames')
        print('b = JamesJamesJamesJamesJames')
        print('c = Error: invalid syntax')
        answer = input("Question 1 Choose the option:  ")
        if answer.lower() == 'a':
            score += 1
        else:
            print()
        print('sampleList = ["Jon", "Kelly", "Jessa"]\n'
              'sampleList.append(2, "Scott")\n'
              'print(sampleList)\n')
        print('a = [‘Jon’, ‘Kelly’, ‘Scott’, ‘Jessa’]')
        print('b = [‘Jon’, ‘Kelly’, ‘Jessa’, ‘Scott’]')
        print('c = TypeError:')
        answer = input("Question 2 Choose the option:  ")
        if answer.lower() == 'c':
            score += 1
        else:
            print()
        print('sampleSet = {"Jodi", "Eric", "Garry"}\n'
              'sampleSet.add(1, "Vicki")\n'
              'print(sampleSet)')
        print('a = {‘Vicki’, ‘Jodi’, ‘Garry’, ‘Eric’}')
        print('b = TypeError:')
        print('c = {‘Jodi’, ‘Vicki’, ‘Garry’, ‘Eric’}')
        answer = input("Question 3 Choose the option:  ")
        if answer.lower() == 'b':
            score += 1
        else:
            print()
        print('p, q, r = 10, 20 ,30\n'
              'print(p, q, r)')
        print('a = 10 20 30')
        print('b = Error:')
        print('c = 20 30 10 ')
        answer = input("Question 4 Choose the option:  ")
        if answer.lower() == 'a':
            score += 1
        else:
            print()
        print('res = "pynative"\n'
              'print(res[1:3])')
        print('a = yna')
        print('b = yn')
        print('c = nat')
        answer = input("Question 5 Choose the option:  ")
        if answer.lower() == 'b':
            score += 1
        else:
            print()
        print('var= "James Bond"\n'
              'print(var[2::-1])')
        print('a = Jam')
        print('b = mes ')
        print('c = maJ')
        answer = input("Question 6 Choose the option:  ")
        if answer.lower() == 'c':
            score += 1
        else:
            print()
        print('res = "my name is James bond"\n'
              'print(res.capitalize())')
        print('a = My name is james bond')
        print('b = My Name Is James Bond')
        print('c = Error: invalid syntax')
        answer = input("Question 7 Choose the option:  ")
        if answer.lower() == 'a':
            score += 1
        else:
            print()
        print('aTuple = (100)\n'
              'print(aTuple * 2)')
        print('a = 100')
        print('b = 200')
        print('c = Error: invalid syntax')
        answer = input("Question 8 Choose the option:  ")
        if answer.lower() == 'b':
            score += 1
        else:
            print()
        print('aTuple = ("Orange")\n'
              'print(type(aTuple))')
        print('a = <class str>')
        print('b = <class>')
        print('c = Error: invalid syntax')
        answer = input("Question 9 Choose the option:  ")
        if answer.lower() == 'a':
            score += 1
        else:
            print()
        print('listOne = [20, 40, 60, 80]\n'
              'listTwo = [20, 40, 60, 80]\n'
              'print(listOne == listTwo)\n'
              'print(listOne is listTwo)')
        print('a = False True')
        print('b = True True')
        print('c = True False')
        answer = input("Question 10 Choose the option:  ")
        if answer.lower() == 'c':
            score += 1
        else:
            print()
    result = (score / total_questions) * 100
    print('Congratulation ✅')
    print(f"Your result {score}/{total_questions} 📌")
    print(f'Result percentages: {result}')


