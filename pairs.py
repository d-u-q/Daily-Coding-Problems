def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(p):
    def left(a,b):
        return a
    return p(left)

def cdr(p):
    def right(a,b):
        return b
    return p(right)

if __name__ == "__main__":
    print car(cons(3,4))
    print cdr(cons(3,4))