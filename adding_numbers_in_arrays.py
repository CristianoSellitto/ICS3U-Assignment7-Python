#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in December 2022
# A program that adds all of the numbers in an array and prints it back to the user


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
    # Write the full equation and calculate the answer
    final_answer = 0
    full_equation_text = ""
    for number in range(0, number_of_loops_integer):
        if number == number_of_loops_integer - 1:
            full_equation_text = full_equation_text + str(number_array[number]) + " = "
        else:
            full_equation_text = full_equation_text + str(number_array[number]) + " + "
        final_answer = final_answer + number_array[number]
    # Print the full equation and the final answer as a string
    print("\n" + full_equation_text + str(final_answer))

    print("\nDone.")


if __name__ == "__main__":
    main()
