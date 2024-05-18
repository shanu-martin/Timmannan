import random

N=random.randint(1,10)
print(N)
chances =4
c=['\033[91m1','\033[93m2','\033[92m3']
class Wrong(Exception):
    ''' just not giving anything here'''
    pass

while True:
    try:
        x=int(input('\033[93mGuess the Number Computer is holding ? :\033[0m'))
        if x == N:
            print('you got it !!')
            break
        else:
            raise Wrong
    except ValueError:
        print('\033[91mInvalid Entry\033[0m')
    except Wrong:
        chances-=1
        if(chances == 0 ):
            print(f'\033[91mGame Over\033[0m no chances remaining !')
            break
        print(f"Try Again \t\t\t Remaining chances :{c[chances-1]}")