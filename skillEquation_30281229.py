# Author: Deepali Vinay (30281229)
# Start Date: 24th March 2019
# Last Modified Date: 11th April 2019

# Importing math library
import math


# Functionality: calculate the skill score by the equation


def calculateSkillEquation(fandom_score, hobbies_score, number_of_sports):
    skillScore = 0  # intialize the output list

    temp = 0  # initialize the flag to zero

    # Check for the validity of fandom score and change the flag if validity fails
    if type(fandom_score) is not int or fandom_score <= 0:
        print("Fandom score is not valid, please enter a non zero, non-negative integer")
        temp = 1

    # Check for the validity of hobbies score and change the flag if validity fails
    if type(hobbies_score) is not int or hobbies_score < 0 or hobbies_score % 4 != 0:
        print("Hobbies score is not valid, please enter a non-negative integer which is a multiple of 4")
        temp = 1

    # Check for the validity of number of sports and change the flag if validity fails
    if type(number_of_sports) is not int or number_of_sports < 0:
        print("Number of sports value is not valid, please enter a non-negative integer")
        temp = 1

    # Check if the flag is unchanged then calculate the skill score using the formula
    if temp == 0:
        skillScore = fandom_score * math.sqrt(42 * math.pow(hobbies_score, 2) / (number_of_sports + 1))
        return skillScore  # return the skill score


if __name__ == '__main__':
    FandomScore, HobbiesScore, SportsNum = 1,2,1                                                                # the output should be 18.33030277982336
    print("Fandom Score=", FandomScore, "\nHobbiesScore=", HobbiesScore, "\nSportsNum=", SportsNum)
    print(calculateSkillEquation(FandomScore, HobbiesScore, SportsNum))
