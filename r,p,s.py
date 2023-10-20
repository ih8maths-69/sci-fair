import random
options=['rock','paper','scissors']
a=True
while a:
    com=random.choice(options)
    move=input('rock,paper or scissors:').lower()
    if move in options:
        print('Computer chooses',com)
        if move=='rock' and com=='paper':
            print('you lost L')
        elif move=='paper' and com=='scissors':
            print('you lost L')
        elif move=='sciossors' and com=='rock':
            print('you losty L')
        elif move==com:
            print('its a tie')
        else:
            print('You won!')
        again=input('wanna play again? Y/n').lower()
        if again=='n':
            a=False
    else:
        print('type rock,paper or scissors')
