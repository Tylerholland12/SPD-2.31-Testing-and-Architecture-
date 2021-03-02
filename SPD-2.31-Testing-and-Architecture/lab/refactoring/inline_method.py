# by Kami Bigdely
# Inline method.
"""
define constants
"""
LEGAL_DRINKING_AGE = 18
class Person:
    """
    Define person attributes
    """
    def __init__(self, my_age):
        self.age = my_age

def enter_night_club(individual):
    """
    logic for verifying age of entry to a club
    """
    if individual.age > LEGAL_DRINKING_AGE:
        print("Allowed to enter.")
    else:
        print("Enterance of minors is denited.")

person = Person(19)
enter_night_club(person)
