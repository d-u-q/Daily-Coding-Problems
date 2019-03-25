from random import randint

repeat = True

while repeat:
    r = raw_input('Enter your roll: ').split('d')
    rolls = [randint(1, int(r[1])) for rolls in range(int(r[0]))]
    print(str(rolls) + ' = ' + str(sum(rolls)))
    rep = raw_input('again? ')
    if rep.startswith('n'):
        repeat = False