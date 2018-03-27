# Project: Input Validation


def collatz(number):
    if number % 2 == 0:
        ret_number = number // 2
    else:
        ret_number = 3 * number + 1

    print(ret_number)
    return ret_number


def _main():
    while True:
        try:
            number = int(input('Please enter an integer number: '))
            break
        except ValueError:
            print('You have to enter an integer value.', end='\n\n')

    while True:
        number = collatz(number)
        if number == 1:
            break


if __name__ == '__main__':
    _main()
