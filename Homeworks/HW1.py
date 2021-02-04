def swap_half_of_list(list_to_swap):
    length_of_the_list = len(list_to_swap)
    for i in range(0, int(length_of_the_list / 2)):
        swap_element = list_to_swap[i]
        list_to_swap[i] = list_to_swap[-(i+1)]
        list_to_swap[-(i+1)] = swap_element
    print(list_to_swap)


def print_specific_even_numbers(last_number):
    for number in range(last_number):
        if number % 2 == 0:
            print(number, end=" ")


if __name__ == '__main__':
    list_of_strings = ["artificial", "intelligence", "data","classification", "methods"]
    list_of_integers = list(range(10))
    swap_half_of_list(list_of_strings)
    number_to_enter = int(input("Please enter a number to print all even numbers up to this number: "))
    print_specific_even_numbers(number_to_enter)
