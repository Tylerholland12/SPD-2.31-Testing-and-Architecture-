# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
"""
MOD DOCSTRING
"""
class Employer:
    """
    CLASS DOCSTRING
    """
    def __init__(self, name):
        self.name = name
    def send(self):
        """
        FUNC DOCSTRING
        """
        print("Students' contact info were sent to", self.name + '.')

class Student:
    """
    CLASS DOCSTRING
    """
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        """
        FUNC DOCSTRING
        """
        return self.gpa
    def send_congrat_email(self):
        """
        FUNC DOCSTRING
        """
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    """
    CLASS DOCSTRING
    """
    def __init__(self, students) -> None:
        self.students = students
    def process_graduation(self):
        """
        FUNC DOCSTRING
        """
        # Find the students in the school who have successfully graduated.
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for person in self.students:
            if person.get_gpa() > min_gpa:
                passed_students.append(person)

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for person in passed_students:
            print(person.name)
        print('****************************')
        # Send congrat emails to them.
        for person in passed_students:
            person.send_congrat_email()


class_students = [Student(2.1, 'Pinocchio'), Student(2.3, 'goku'), Student(2.7, 'toro'),
            Student(3.9, 'naruto'), Student(3.2,'Layl'), Student(3,'Bondf')]
school  = School(class_students)
school.process_graduation()
