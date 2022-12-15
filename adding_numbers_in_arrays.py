#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# A program that adds all of the numbers in an array and prints it back to the user


def add_numbers_in_arrays(array):
    # Adds all of the numbers in an array

    sum = 0
    for number in array:
        sum += number

    return sum


def format_adding_array_text(array):
    # Formats the sum text of an array

    equation_text = ""
    for number in range(0, len(array)):
        if number == len(array) - 1:
            equation_text += str(array[number]) + " = "
        else:
            equation_text += str(array[number]) + " + "

    return equation_text


def main():
    # Adds all of the numbers in an array and prints it back to the user

    # Set the number of loops if it is a valid integer
    while True:
        try:
            number_of_loops_text = input(
                "\nEnter the amount of numbers you want in the array: "
            )
            number_of_loops_integer = int(number_of_loops_text)
            break
        except ValueError:
            print("\nYou did not enter a valid integer.")
    # Append the inputted number to the array if it is a valid integer
    number_array = []
    for counter in range(0, number_of_loops_integer):
        try:
            print(
                "\nNumber of inputs left: {}".format(number_of_loops_integer - counter)
            )
            number_text = input("Enter a number: ")
            number_value = float(number_text)
            # For formatting integers
            if number_value % 1 == 0:
                number_value = int(number_value)
            number_array.append(number_value)
        except ValueError:
            print("\nYou did not enter a valid number.")
    final_answer = add_numbers_in_arrays(number_array)
    full_equation_text = format_adding_array_text(number_array)
    # Print the full equation and the final answer as a string
    print("\n" + full_equation_text + str(final_answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
