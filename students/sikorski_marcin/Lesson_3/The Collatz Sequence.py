def collatz(number):
    is_it_dividable_by_two = number % 2
    if is_it_dividable_by_two == 0:
        return number // 2
    elif is_it_dividable_by_two == 1:
        return 3 * number + 1
    else:
        print("What sort of input is this???")

number_to_check = float(input("Enter a number for a collatz sequence: "))
is_this_number_one = collatz(number_to_check)

print(number_to_check)  
print(is_this_number_one)
while is_this_number_one != 1:
    print(collatz(is_this_number_one))
    is_this_number_one = collatz(is_this_number_one)