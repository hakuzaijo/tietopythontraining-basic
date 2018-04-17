def print_options():
    print("Welcome to organized calculator:")
    print("a - add")
    print("s - subtract")
    print("m - multiply")
    print("d - divide")
    print("p - power")
    print("h,? - help")
    print("q - QUIT")


def calculate():
    while True:
        print("Enter option:")

        option = input()

        if option == "a":
            add()

        if option == "s":
            subtract()

        if option == "m":
            multiply()

        if option == "d":
            divide()

        if option == "p":
            power()

        if option == "h":
            print_options()

        if option == "?":
            print_options()

        if option == "q":
            print("GOOD BYE")
            break


def power():
    print("POWER")
    add_var_1, add_var_2 = get_inputs()
    print("Result:")
    print(add_var_1 ** add_var_2)


def divide():
    print("DIVIDE")
    add_var_1, add_var_2 = get_inputs()
    print("Result:")
    print(add_var_1 / add_var_2)


def multiply():
    print("MULTIPLY")
    add_var_1, add_var_2 = get_inputs()
    print("Result:")
    print(add_var_1 * add_var_2)


def subtract():
    print("SUBTRACT")
    add_var_1, add_var_2 = get_inputs()
    print("Result:")
    print(add_var_1 - add_var_2)


def add():
    print("ADDING")
    add_var_1, add_var_2 = get_inputs()
    print("Result:")
    print(add_var_1 + add_var_2)


def get_inputs():
    print("Input 1st operand:")
    add_var_1 = int(input())
    print("Input 2nd operand:")
    add_var_2 = int(input())
    return add_var_1, add_var_2


if __name__ == '__main__':
    print_options()
    calculate()
