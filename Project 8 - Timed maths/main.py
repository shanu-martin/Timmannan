import random
import sys
import time

#Constants
n=10
operators = ['+','-','*']
atmpts = 1
#functions
def builder():
    exp = f'{random.randint(1,10)} {random.choice(operators)} {random.randint(5,15)}'
    ans = eval(exp)
    return exp,ans
start_time = time.time()
for i in range(n):
    exp,ans = builder()
    while True:
        guess = input(f'Q{i+1} \033[96m{exp} = \033[0m ')
        if guess == str(ans):
            atmpts = 1
            break
        else:
            sys.stdout.write('\033[0F')
            sys.stdout.write('\033[K')
            sys.stdout.flush()
            atmpts +=1
            print(f'\033[91mAttempt no -{atmpts}: \033[0m',end='')
            if atmpts == 10:
                print('\033[2J\033[H\033[91m', end='Game Over')
                end_time = time.time()
                print(f' time taken {round(end_time-start_time,2)} Seconds...')
                sys.exit()
end_time = time.time()
print(f'Congratulations you finished in {round(end_time-start_time,2)} Seconds...')
       