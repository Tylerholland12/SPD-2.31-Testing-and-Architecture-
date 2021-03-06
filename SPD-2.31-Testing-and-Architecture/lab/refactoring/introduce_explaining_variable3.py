# by Kami Bigdely
# Extract Variable (alias introduce explaining variable)
"""
leading docstring
"""
WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05

def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    """
    function docstring
    """
    t_t_p = time * temperature * pressure
    well = t_t_p * COOKED_CONSTANT >= WELL_DONE
    medium = t_t_p * COOKED_CONSTANT >= MEDIUM
    
    if desired_state == well:
        return True
    if desired_state == medium:
        return True
    return False
