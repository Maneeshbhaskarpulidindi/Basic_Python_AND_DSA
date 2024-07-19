import sys

#print(sys.getrecursionlimit())
#sys.setrecursionlimit(100)

i = 0
print(i)
def geet():
    globals()['i'] = globals()['i'] + 1
    print(globals()['i'] )
    geet()



def geet_using_the_gobal():
    global i
    try:
        i = i+1
        geet_using_the_gobal()
    except RecursionError:
        print(f'The maximum recursion depth has been exceeded. Current value of i is {i}')


def factorial(number):
    if number ==1: return 1
    else: return number*factorial(number -1)



if __name__ == '__main__':
    #geet_using_the_gobal()
    #geet()
    #print(i)
    number = int(input('Number -> '))
    print(" Number : {} and Result : {}".format(number, factorial(number)))
