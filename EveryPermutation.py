# Problem 96
import random,math,copy
# Fun, inefficient solution
def EveryPermutationF(l):
    max = math.factorial(len(l))
    ret = []
    ret.append(copy.copy(l))
    while len(ret) < max:        
        random.shuffle(l)
        if l not in ret:
            ret.append(copy.copy(l))            
    return ret
            

if __name__ == "__main__":
    print(EveryPermutationF([1,2,3]))