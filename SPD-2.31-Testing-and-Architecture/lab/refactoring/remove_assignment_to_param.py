# By Kami Bigdely
# Remove assignment to method parameter.
"""
LEADING DOCSTRING
"""
class Distance:
    """
    CLASS DOCSTRING
    """
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value
class Mass:
    """
    CLASS DOCSTRING
    """
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit
def calculate_kinetic_energy(mass, distance, time):
    """
    FUNC DOCSTRING
    """
    if distance.unit != 'km':
        if distance.unit == "ly":  # [ly] stands for light-year (measure of distance in astronomy)
            # convert from light-year to km unit
            in_km = distance.value * 9.461e12
            distance = Distance(in_km, "km")
        else:
            print ("unit is Unknown")
            return distance
    speed = distance.value/time # [km per sec]
    if mass.unit != 'kg':
        if mass.unit == "solar-mass":
            # convert from solar mass to kg
            value = mass.value * 1.98892e30 # [kg]
            mass = Mass(value, 'kg')
        else:
            print ("unit is Unknown")
            return mass

    kinetic_energy = 0.5 * mass.value * speed ** 2
    return kinetic_energy

mass_to = Mass(2, "solar-mass")
distance_to = Distance(2, 'ly')
print(calculate_kinetic_energy(mass_to, distance_to, 3600e20))
