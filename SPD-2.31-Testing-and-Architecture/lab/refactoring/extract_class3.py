# by Kami Bigdely
# Extract class
WELL_DONE = 3000
MEDIUM = 2500
COOKED_CONSTANT = 0.05

class Cook:
    def __init__(self, time, temperature, pressure, desired_state):
        self.time = time
        self.temp = temperature
        self.pressure = pressure
        self.desired_state = desired_state
    
    def is_cookeding_criteria_satisfied(self):
        return self.is_well_done() or self.is_medium()


    def is_well_done(self):    
        return self.desired_state == 'well-done' and  \
               self.get_cooking_progress() >= WELL_DONE


    def is_medium(self):
        return self.desired_state == 'medium' and  \
               self.get_cooking_progress() >= MEDIUM

    def get_cooking_progress(self):
        return self.time * self.temp * self.pressure * COOKED_CONSTANT


time = 30 # [min]
temp = 103 # [celcius]
pressure = 20 # [psi]
desired_state = 'well-done'
cookied_criteria = Cook(time, temp, pressure, desired_state)
if cookied_criteria.is_cookeding_criteria_satisfied():
    print('cooking is done.')
else:
    print('ongoing cooking.')