#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: September 2019
# This program finds the largest number in an array


import random


def calculate(array_of_numbers):
    # This function finds the largest number in a list

    # Variables
    large_number = 0

    # Process
    for counter in range(len(array_of_numbers)):
        if array_of_numbers[counter] > large_number:
            large_number = array_of_numbers[counter]

    # Output
    return large_number


def main():
    # This function creates an array of 10 numbers then prints out the largest

    # Array
    number_array = []

    # Adding numbers to an array
    for counter in range(10):
        random_number = random.randint(1, 100)
        print(random_number)
        number_array.append(random_number)

    # Process
    largest_number = calculate(number_array)

    # Output
    print("")
    print("The largest number in the array is", largest_number)


if __name__ == "__main__":
    main()
