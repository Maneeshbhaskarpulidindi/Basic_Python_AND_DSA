from  functools  import  reduce
def Using_filterr():
    nums= [1,2,3,4,5]
    evens = list(filter(lambda x:x%2==0,nums))
    odds = list(filter(lambda x:x%2==1,nums))
    print("Evens: ", evens)
    print("Odds: ", odds)
    return evens, odds

def Using_MApi():
    evvens , odds = Using_filterr()
    doubles = list(map(lambda x: x*2,evvens))
    print("Doubles: ", doubles)
    sum=reduce(lambda s,b :s+b,doubles)
    print("Sum: ", sum) 


if __name__ == "__main__":
    Using_MApi()

