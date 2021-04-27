#!/usr/bin/env python3
# Created by: Brian Musembi
# Created on: 27 April 2021
# This program calculates the circumference of a circle
#   with user input

import constants


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("Circumference is {} mm2.".format(circumference))
    print("\nDone.")


if __name__ == "__main__":
    main()
