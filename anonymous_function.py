# Problem 91
 
functions = []
for i in range(10):                 # loops 10 times
    functions.append(lambda : i)    # appends "9" because i is 9 after the loop

# for f in functions:
#    print(f())

i=0                                 
for f in functions:                 
    print(f())
    i+=1                            # fix by printing incremented i