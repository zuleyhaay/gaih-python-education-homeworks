# Function to check if the number divided by a number in range.
def is_divided_number(numb, division):
    is_divided = False

    if numb % division == 0:
        is_divided = True

    return is_divided


# Function to check if the number in range is prime number
def is_prime_number(numb, num_range):
    is_prime = False
    if number > 2:
        for division in range(2, num_range):
            if numb > division:
                if is_divided_number(numb, division):
                    is_prime = False
                    break
                else:
                    is_prime = True
            else:
                break
    elif number == 2:
        is_prime = True

    return is_prime


if __name__ == '__main__':
    for number in range(100):
        if is_prime_number(number, 100):
            print(number, end=" ")
