
if __name__ == '__main__':
    square = lambda x: x * x
    cube = lambda x: x ** 3
    add = lambda a, b: a + b

    while True:
        user_input = input()
        if user_input == 'exit':
            break
        elif user_input == 'add':
            a, b = map(int, input("Enter two numbers to add, separated by space: ").split())
            e = add(a, b)
            print(e)
        elif user_input == 'cube':
            x = int(input("Enter a number to cube: "))
            print(cube(x))
        elif user_input == 'square':
            x = int(input("Enter a number to square: "))
            print(square(x))
        else:
            print("Unknown command. Please enter 'add', 'cube', 'square', or 'exit'.")

