# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
"""
Import math library
"""
import math

def print_stat():
    """
    write the logic for printing the stats of the class grades
    """
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))

    mean = calculate_mean_grade(grade_list)
    s_d = calculate_s_d(grade_list, mean)

    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(s_d, 3))
    print('****** END ******')

def calculate_mean_grade(grade_list):
    """
    Calculate the mean scores
    """
    grades_sum = 0
    
    for grades in grade_list:
        grades_sum = grades_sum + grades
    
    mean = grades_sum // len(grade_list)
    return mean

def calculate_s_d(grade_list, mean):
    """
    Calculate the standard deviation
    """
    s_d = 0
    sqrs_sum = 0

    for grades in grade_list:
        sqrs_sum+=(grades - mean) ** 2

    s_d = math.sqrt(sqrs_sum // len(grade_list))

    return s_d
