# Kami Bigdely
# Move Field

class Car:
    def __init__(self, engine, wheels, cabin, fuel_tank):
        self.engine = engine
        # TODO: tpms is better to be in the Wheel class.
        # Each wheel has a single tpms attached to it.
        # Thus, instead of having a list of tpms in 'Car' class
        # have each of the tpms in each 'Wheel'.
        # self.tpms_list = tpms_di  # Tire Pressure Monitoring System.
        self.wheels = wheels
        # Set wheels' car reference into each wheel.
        for w in wheels:
            w.set_car(self)

        self.cabin = cabin
        self.fuel_tank = fuel_tank


class Wheel:
    # TODO: You may add tpms as a method parameter here to
    #       initilaize the 'Wheel' object or you can create
    #       a setter method to set the tpms of the wheel. (you can do
    #       both of course.)
    def __init__(self, tmps,  car = None, wheel_location = None):
        self.car = car
        self.wheel_location = wheel_location
        self.tmps = tmps

    def install_tire(self):
        print('remove old tube.')
         # TODO: Rewrite the following after moving tpms to the 'Wheel' class
        print('cleaned tpms: ',
              self.tmps.get_serial_number,
              '.')
        print('installed new tube.')        
        
    def read_tire_pressure(self):
        # TODO: After making tpms an attribute of 'Wheel' class,
        #       rewrite the following.
        return self.tmps.get_pressure()
    
    def set_car(self, car):
        self.car = car


class Tpms:
    """Tire Pressure Monitoring System.
    """
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.sensor_transmit_range = 300 # [feet]
        self.sensor_pressure_range = (8,300) # [PSI]
        self.battery_life = 6 # [year]
        
    def get_pressure(self):
        return 3
    
    def get_serial_number(self):
        return self.serial_number
    
class Engine:
    def __init__(self):
        pass
    
class FuelTank:
    def __init__(self):
        pass
    
class Cabin:
    def __init__(self):
        pass    
    

engine = Engine()
# TODO: Rewrite the following after moving tpms to the 'Wheel' class.
wheels = [Wheel(Tpms(983408543), None, 'front-right'), 
          Wheel(Tpms(4343083), None, 'front-left'), 
          Wheel(Tpms(23654835), None, 'back-right'), 
          Wheel(Tpms(3498857), None, 'back-left')]

cabin  = Cabin()

fuel_tank = FuelTank()

my_car = Car(engine, wheels, cabin, fuel_tank)


