import time
def testFunc():
    print 'Hello World'

def schedF(f,n):
    print 'Scheduler started'
    time.sleep(n/1000)
    print ('Waited %d milliseconds' % n)
    f()

if __name__ == "__main__":
    schedF(testFunc,4000)