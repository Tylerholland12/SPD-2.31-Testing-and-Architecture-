# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
# Refactored.
import math 
import pytest

def display_grade_stat():
    """Gathers stats and print them out."""
    grade_list = read_input()
    # Calculate the mean and standard deviation of the grades
    mean, standard_deviation = calculate_stat(grade_list)
    # print out the mean and standard deviation in a nice format.
    print_stat(mean, standard_deviation)

def read_input():
    """Get the inputs from the user."""
    grade_list = []
    n_student = 5
    for grade_number in range(0, n_student):
        question = 'Enter grade #{}: '.format(grade_number+1)
        grade_list.append(int(input(question)))
    return grade_list

def calculate_stat(grade_list):
    """Calculate the mean and standard deviation of the grades."""
    total = 0
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list)) # standard deviation
    return mean, sd

def print_stat(mean, sd):
    """print out the mean and standard deviation in a nice format."""
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')


# TESTS
@pytest.mark.parametrize("grade_list,expected_mean,expected_sd", [
    ([10, 10, 10, 10], 10, 0),
])
def test_calculate_stat(grade_list, expected_mean, expected_sd):
    """Test the function works on a Continuous uniform distribution
    (aka one where all the values are the same)."""
    actual_mean, actual_sd = calculate_stat(grade_list)
    assert actual_mean == expected_mean
    assert actual_sd == expected_sd