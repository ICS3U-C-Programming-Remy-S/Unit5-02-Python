#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Nov 28, 2023
# This program will ask user for the base and
# height of a triangle and display the area
# using a multiple functions


def calc_area_triangle(base, height):
    # calculate area
    area = (base * height) / 2

    # display area to user
    print(f"\n{base}cm x {height}cm = {area}cm^2")


def main():
    # Get base and height from user and display message about program
    print("This program will ask user for the base and ")
    print("height of a triangle and display the area in cm.")
    user_base_str = input("Please enter base of triangle(cm): ")
    user_height_str = input("Please enter height of triangle(cm): ")

    # Catch if the user entered a string
    try:
        # Convert base as a string to float
        user_base_float = float(user_base_str)

        # Convert height as a string to float
        user_height_float = float(user_height_str)

    except Exception:
        # Message for invalid user number
        print(
            "\n{} are not valid base and height.".format(user_base_str, user_height_str)
        )

    # Call the fahrenheit function
    calc_area_triangle(user_base_float, user_height_float)


if __name__ == "__main__":
    main()
