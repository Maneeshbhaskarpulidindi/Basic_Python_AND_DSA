def ALL_hash(num):
    for i in range(num):
        print("####")

def incresing_hash(num):
    for i in range(num):
        print("#"*(i+1))

def decreasing_hash(num):
    for i in range(num):
        print("#"*(num-i))

"""
1 2 3 4 
2 3 4
2 4 
4
"""
def differnt_pattern(num):
    for i in range(num):
        """j =i 
        while  j <=num:
            print(j,end=" ")
            j+=1
        print()"""
        for j in range(i,num):
            print(j+1, end=" ")
        print()
        



"""
4 3 2 1
4 3 2 
3 2 
1
"""
def differnt_pattern_2(num):
    for i in range(num):
        j =num 
        while  j>i:
            print(j,end=" ")
            j-=1
        print()

""" 
4 
4 3 
4 3 2 
4 3 2 1
"""

def differnt_pattern_3(num):
    for i in range(num):
        for j in range(i+1):
            print(num-j, end=" ")
        print()


"""
   #
  ###
 #####
"""

def pattern_pyramid(num):
    for i in range(num):
        print(" "*(num-i-1) + "#"*(2*i+1))

if __name__ == "__main__":
    num=4
    differnt_pattern(num)
    print("done")
    differnt_pattern_2(num)
    print("done")
    differnt_pattern_3(num)
    print("done")
    pattern_pyramid(num)
    print("done")
    ALL_hash(num)
    print("done")
    incresing_hash(num)
    print("done")
    decreasing_hash(num)




