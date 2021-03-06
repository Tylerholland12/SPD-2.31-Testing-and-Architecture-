# by Kami Bigdely
# Inline method.
"""
MOD DOCSTRING
"""
class Person:
    """
    Define person attributes
    """
    def __init__(self, my_age):
        self.age = my_age
        self.LEGALDRINKINGAGE = 18

    def enter_night_club(self, age):
        """
        logic for verifying age of entry to a club
        """
        if over_18(self.age):
            print("Enter")
        else:
            print("People under the age of 18 cannot enter.")

    def over_18(self, age):
        if age > self.LEGALDRINKINGAGE:
            return True
        else:
            return False

person = Person(19)
person.enter_night_club(person)