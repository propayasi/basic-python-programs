import time
def coll(x):
    while x != 1:
        print(x)
        if x % 2 == 0:
            x = int(x / 2)
        else:
            x = int(3 * x + 1)
    else:
        print(x)
        print('Done!')


def main():
    x = int(input('Input an integer: '))
    starttime=time.time()
    coll(x)
    print('time taken %s seconds'%(time.time()-starttime))
main()