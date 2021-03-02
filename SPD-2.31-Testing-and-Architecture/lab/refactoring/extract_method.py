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

    # Calculate the mean and standard deviation of the grades
    grade_sum = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        grade_sum = grade_sum + grade
    mean = grade_sum / len(grade_list)
    s_d = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    s_d = math.sqrt(sum_of_sqrs / len(grade_list))
    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(s_d, 3))
    print('****** END ******')

print_stat()
