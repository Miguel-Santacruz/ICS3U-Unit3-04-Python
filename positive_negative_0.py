#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: March 2022
# This program says the sign of an integer


def main():
    # This function says the sign of an integer

    # Input
    number = int(input("Enter an integer: "))

    # Process & Output
    print("")
    if number > 0:
        print("{} is positive!".format(number))
    elif number < 0:
        print("{} is negative!".format(number))
    else:
        print("{} is zero!".format(number))

    print("\nDone.")


if __name__ == "__main__":
    main()
