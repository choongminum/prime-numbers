"""
Choong Min Um <choongmin.um@unh.edu>

This demo module finds prime numbers between two numbers.
"""

import argparse


def find_prime(num1, num2):
    for n in range(num1, num2 + 1):
        for x in range(2, n):
            if n % x == 0:
                print(n, "is equal to", x, "*", n // x)
                break
        else:
            # loop fell through without finding a factor
            print(n, "is a prime number")


def def_args():
    parser = argparse.ArgumentParser(
        description=(
            "This demo module finds prime numbers between two numbers."
        )
    )

    # Define positional arguments.
    parser.add_argument("num1", type=int, help="first number")
    parser.add_argument("num2", type=int, help="second number")

    args = parser.parse_args()
    return args


def main():
    args = def_args()
    result = find_prime(args.num1, args.num2)


if __name__ == "__main__":
    main()
