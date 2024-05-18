import pandas as pd
import random
class Exit(Exception):
    ''' just not giving anything here'''
    pass
z=('''\033[2J\033[HWelcome Player 1
We assume you known the rules!\t\t
Enter \033[91m0 to exit\033[0m \n''')
print(z)

l=[['D','L','W'],['W','D','L'],['L','W','D']]
ul=['Urock','Upaper','Uscissor']
com=['rock','paper','scissor']
x=pd.DataFrame(l,columns=com,index=ul)
res_user=0
res_com=0
def validator(x):
    global res_com
    global res_user
    if x=='D':
        print('it`s a Draw')
    elif x== 'W':
        print('You won this Round!',end='')
        res_user+=1
        # print(f'\t\tCurrent score : User -{res_user}\tCom - {res_com}')
    else:
        print('You lost this Round!',end='')
        res_com+=1
        # print(f'\t\tCurrent score : User -{res_user}\tCom - {res_com}')
        

while True:
    try:
        print(f'\t\t\tCurrent score : User {res_user}\tCom {res_com}')
        user_entry=int(input('Make your choice from \n\033[96mROCK : 1 \t\033[93mPAPER : 2 \t\033[92mSCISSOR :3\n\033[0mEnter corresponding Numbers to your choice :'))
        if user_entry == 0:
            raise Exit
        user=ul[user_entry-1]
        com_choice =random.choice(com)
        validator(x.loc[user,com_choice])

    except Exit:
        print('\033[93mU Quit.....so Computer won\033[0')
        break
    except Exception:
        print("\033[91mInvalid Entry\033[0m")

    except ValueError:
        print("\033[91mInvalid Entry\033[0m")