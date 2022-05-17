#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 16 2022
# rounds a number


def roundDecimal(decimal_number, decimal_amount):
    # round decimal
    decimal_number[0] = decimal_number[0] * (10 ** decimal_amount[0]) + 0.5
    decimal_number[0] = int(decimal_number[0])
    decimal_number[0] = decimal_number[0] / (10 ** decimal_amount[0])


def main():
    # Lists
    number = []
    decimal = []
    try:
        # Inputs
        users_num = float(input("Enter the number you want to round: "))
        decimal_place = int(
            input("Enter the amount of decimal places " "you want to round to: ")
        )
        if decimal_place < 0:
            print("You have to input an integer above 0")
        else:
            # add to the list
            number.append(users_num)
            decimal.append(decimal_place)
            # call the function
            roundDecimal(number, decimal)
            print("The number rounded is {}".format(number[0]))
    except:
        print("You have to input a number")


if __name__ == "__main__":
    main()
