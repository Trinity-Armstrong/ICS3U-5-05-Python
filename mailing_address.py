#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This program formats Canadian mailing addresses


def mailing_address(name, address, city, province, postal_code,
                    apartment=None):
    # This function formats the mailing address

    # Process
    if apartment is not None:
        formatted_address = name + "\n" + apartment + "-" + address + "\n" + \
                       city + " " + province + "  " + postal_code
    else:
        formatted_address = name + "\n" + address + "\n" + city + \
                       " " + province + "  " + postal_code

    return formatted_address


def main():
    # This function gets information, calls other functions and prints address

    # Variables
    user_apartment_number = None

    # Input
    print("This program formats Canadian mailing addresses.")
    print("Please enter the following information:")
    print("")
    user_name = input("Full name: ")
    user_address = input("Address (street number & street name): ")
    question = input("Do you live in an apartment? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        user_apartment_number = input("Apartment number: ")
    user_municipality = input("Municipality: ")
    user_province = input("Province/Territory (abbreviate): ")
    user_postal_code = input("Postal code: ")

    # Process
    if user_apartment_number is not None:
        address = mailing_address(user_name, user_address,
                                  user_municipality, user_province,
                                  user_postal_code, user_apartment_number)
    else:
        address = mailing_address(user_name, user_address,
                                  user_municipality, user_province,
                                  user_postal_code)

    # Output
    print("")
    print(address)


if __name__ == "__main__":
    main()
