def using_only_for(nums):
    for i in nums:
        if i % 5==0:
            print(i)
            break # if only one number
        else:
            print("not found") # prints so many times

def using_For_and_else(nums):
    for i in nums:
        if i % 5 == 0:
            print(i)
    else:
        print("not found")



if __name__ == '__main__':
    nums = [12,15, 18, 19, 20, 21, 22, 23]
    using_only_for(nums)
    print("---") # prints a separator for each function call
    using_For_and_else(nums)








