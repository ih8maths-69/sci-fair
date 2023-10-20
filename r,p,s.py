options=('rock','paper','scissors')
import random
a=True
while a:
    move=input('rock,paper or scissors:').lower()
    com=random.choice(options)
    if move:
        print(com)
        
    else:
        print('type rock,paper or scissors')
    if move=='rock' and com=='paper':
        print('You lost L')
    elif move=='paper' and com=='scissors':
        print('You lost L')
    elif move=='scissors'and com=='rock':
        print('you lost L')
    else:
        print('You won!')
    again=input('Wanna play again? type Y/n:').lower()
    if again=='n':
        a=False