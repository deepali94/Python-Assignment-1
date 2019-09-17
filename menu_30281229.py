# Author: Deepali Vinay (30281229)
# Start Date: 24th March 2019
# Last Modified Date: 11th April 2019


"""Functionality: An interactive menu, that takes the input from the user
and returns back to the menu, validates each user input,
and gives output accordingly."""

# Importing math library
import math

while True:  # infinite loop

    # Printing the options of the menu
    print(" ----------------------------------- \n" +
          "|Menu:\n" +
          "|1: Enter Fandom score\n" +
          "|2: Enter Hobbies score\n" +
          "|3: Enter Number of sports played\n" +
          "|4: Calculate nerd score\n" +
          "|5: Print nerd rating\n" +
          "|6: To exit menu\n" +
          "|7: Reset the inputs\n" +
          " ----------------------------------- ")

    # Taking the menu input from the user
    menu_input = input("Enter choice : ")

    # Validating the menu input
    if not menu_input.isdigit() or int(menu_input) <= 0:  # validation: if input a string/negative/float,retake  input
        print("Invalid Input, try again")
        continue                                          # going back to the beginning of the while loop
    else:
        menu_input = int(menu_input)                      # changing the input type from string to integer

    # Fandom score
    if menu_input == 1:

        # Printing the instructions for the input
        print("Fandom Score is the number of things that the person considers them-self a ‘fan of’.\nFor example,"
              "if you like both Star Wars and Star Trek but nothing else, then you have a score of 2")

        while True:  # infinite loop till input is valid

            # Taking the fandom score input from the user
            fandom_score = input("Enter the number of things that you are a fan of : ")

            # Validating the input
            if not fandom_score.isdigit():  # validation: if input is string/negative/float, retake the input
                print("Invalid input, input cannot be a floating point or a negative number or a string, re-enter!")
            elif int(fandom_score) == 0:    # validation: if input is zero, retake the input
                print("Invalid input, input cannot be zero, re-enter!")
            else:                           # validation: if input in non-zero, non-negative,integer, consider the input
                fandom_score = int(fandom_score)  # changing the input type from string to integer
                break                       # to come out of the while loop after stroring input in a variable

    # Hobbies score
    elif menu_input == 2:

        # Printing the instructions for the input
        print("Your Hobbies Score is the number of hobbies you undertake every week.\nYou are expected to enter a "
              "monthly score, assuming 4 weeks in a month, the input should be a multiple of 4")

        while True:  # infinite loop till input is valid

            # Taking the hobbies score input from the user
            hobbies_score = input("Enter the number of hobbies you undertake per month : ")

            # Validating the input
            if not hobbies_score.isdigit():     # validation: if input is string/negative/float, retake the input
                print("Invalid input, input cannot be a floating point or a negative number or a string, re-enter!")
            elif int(hobbies_score) % 4 != 0:   # validation: if input is a multiple of 4
                print("Invalid input, input should be a multiple of 4 including zero, re-enter!")
            else:                               # valodation: if input is int,positive, and in multiples of number 4
                hobbies_score = int(hobbies_score)  # changing the input type from string to integer
                break                           # to come out of the while loop after stroring input in a variable

    # Number of sports
    elif menu_input == 3:

        # Printing the instructions for the input
        print("A person is considered to play a sport if they own an item that could be used in that sport. \nIf a "
              "person owns a soccer ball then their score is 1. \nIf an item can be used for multiple sports, "
              "then it only counts as 1 towards this number.")

        while True:  # infinite loop till input is valid

            # Taking the number of sports input from the user
            number_of_sports = input("Enter number of sports played : ")

            # Validating the input
            if not number_of_sports.isdigit():  # validation: if input is string/negative/float, retake the input
                print("Invalid input, input cannot be a floating point or a negative number or a string, re-enter!")
            else:                               # validation: if input is a positive integer
                number_of_sports = int(number_of_sports)  # changing the input type from string to integer
                break                           # to come out of the while loop after stroring input in a variable

    # Calculate nerd score
    elif menu_input == 4:
        temp = 0  # initialize the flag to zero

        # Check if fandom score is provided by the user and change the flag otherwise
        if "fandom_score" not in globals():
            print("Fandom score missing!!")
            temp = 1

        # Check if hobbies score is provided by the user and change the flag otherwise
        if "hobbies_score" not in globals():
            print("Hobbies score is missing!!")
            temp = 1

        # Check if number of sports is provided by the user and change the flag otherwise
        if "number_of_sports" not in globals():
            print("Number of sports played is missing!!")
            temp = 1

        # Check if the flag is unchanged then calculate the skill score using the formula
        if temp == 0:
            nerd_score = fandom_score * math.sqrt(42 * math.pow(hobbies_score, 2) / (number_of_sports + 1))
            print("Your nerd score is : ", nerd_score)
            del fandom_score, hobbies_score, number_of_sports   # remove variables after calculation
        else:
            print("Please enter above missing input(s)!")
            continue                                            # to go back to the menu after printing the fandom score

    # Printing the nerd rating
    elif menu_input == 5:

        # Checking if nerd score is calculated
        if "nerd_score" in globals():  # if nerd score is calculated, only then the variable will be declared
            print("Your Nerd rating is xxx")
            del nerd_score             # remove the variable after printing
        else:                          # if no nerd score print an error message
            print("You have not calculated your Nerd Score yet! Please press 4 in the menu to calculate it!!")

    # Exiting the menu
    elif menu_input == 6:
        print("Exiting the menu")
        break                      # break out of the while loop,when the specified input is 6

    # Resetting the inputs
    elif menu_input == 7:

        # initialize variables in formula to avoid NameError before we execute del statement
        fandom_score = hobbies_score = number_of_sports = nerd_score = 0

        #remove all the variables
        del fandom_score, hobbies_score, number_of_sports, nerd_score
        print("Resetting the inputs")

    # Menu input greater than 7
    else:   # if menu imput is greater than 7
        print("Input cannot be greater than 7! Re-enter!")
