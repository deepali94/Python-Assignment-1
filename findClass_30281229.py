# Author: Deepali Vinay (30281229)
# Start Date: 24th March 2019
# Last Modified Date: 11th April 2019


# Functionality: Determine the number of members in each nerd class by iterating through the input studentScore_list

def countStudentClass(studentScore_list):
    if len(studentScore_list) < 1:
        print("Please add at least 1 item into the list")
        return 0

    nerdCount_list = [0] * 7  # initialize the output list

    # Going through each element of the input list studentScore_list
    for score in studentScore_list:

        if type(score) is int or type(score) is float:  # validation: if passed input is float or int
            # Nerdlite
            if score == 0:
                nerdCount_list[0] = nerdCount_list[0] + 1
            # Nerdling
            elif 0 < score < 10:
                nerdCount_list[1] = nerdCount_list[1] + 1
            # Nerdlinger
            elif 10 <= score < 100:
                nerdCount_list[2] = nerdCount_list[2] + 1
            # Nerd
            elif 100 <= score < 500:
                nerdCount_list[3] = nerdCount_list[3] + 1
            # Nerdington
            elif 500 <= score < 1000:
                nerdCount_list[4] = nerdCount_list[4] + 1
            # Nerdrometa
            elif 1000 <= score < 2000:
                nerdCount_list[5] = nerdCount_list[5] + 1
            # Nerd Supreme
            elif score >= 2000:
                nerdCount_list[6] = nerdCount_list[6] + 1
            # Checking for negative numbers
            else:
                print(score, "is an invalid input")
        else:                                           # validation: if passed input is not int/float
            print(score, "is an invalid input")


    return nerdCount_list  # returning the output list


if __name__ == '__main__':
    # test cases
    # studentScore_list = []  #
    studentScore_list = [23, 76, 1300, 600]  # output should be [0, 0, 2, 0, 1, 1, 0]

    print(countStudentClass(studentScore_list))
