import random

no_of_process = random.randint(4,15)

f = open('input.txt', 'w')
f.write(f'{no_of_process}\n')
for i in range(1,no_of_process + 1):
    f.write(f'{i}\n')
    f.write(f'{random.randint(0,15)}\n')
    f.write(f'{random.randint(1, 15)}\n')
f.close()
