repeat = True

while repeat:
    n = raw_input("Enter a number: ")
    ret = 0
    if (n < 10):
        ret = n+1

    print(ret)
    rep = raw_input('again? ')
    if rep.startswith('n'):
        repeat = False