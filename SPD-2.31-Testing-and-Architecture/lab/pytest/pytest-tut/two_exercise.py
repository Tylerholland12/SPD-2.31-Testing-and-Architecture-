import math
import pytest

"""Consider the following function that calculates the age of fossile:"""

T_HALF = 5730
DECAY_CONSTANT = -0.693

def get_age_carbon_14_dating(carbon_14_ratio):
    """Returns the estimated age of the sample in year.
    carbon_14_ratio: the percent (0 < percent < 1) of carbon-14 
    in the sample conpared to the amount in living 
    tissue (unitless). 
    """
    if carbon_14_ratio <= 0:
        raise ValueError("Please put a ratio greater than 0")
    answer = math.log(carbon_14_ratio) / DECAY_CONSTANT * T_HALF
    return math.floor(answer * 100)/100.0

# TODO: Write a unit test which feed 0.35 to the function. 
# The result should be '8680.34'. Does the function handles 
# every possible input correctly? What if the input is zero
# or negative?
# Add the necessary logic to make sure the function handle 
# every possible input properly. Then write a unit test againt 
# this special case.
def test_carbon_14_dating_floats():
    assert math.isclose(get_age_carbon_14_dating(0.35), 8680.34)


def test_carbon_14_dating_errors():
    """Ensures we throw an Exception if the input is out of domain of the log(
    function."""
    with pytest.raises(ValueError):
        get_age_carbon_14_dating(0)
        get_age_carbon_14_dating(-5)
        get_age_carbon_14_dating(-100)