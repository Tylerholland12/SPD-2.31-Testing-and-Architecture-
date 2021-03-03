class Subject:
    """Represents what is being observed"""

    def __init__(self):
        """create an empty observer list"""
        self.observers = []

    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(self, observer):
        pass
        # if observer not in self.observers:
        #     self.observers.append(observer)

    def removeObserver(self, observer):
        pass


    # This method is called to notify all observers
    # when the Subject's state (measuremetns) has changed.
    def notifyObservers(self):
        pass
        # """Notify the observers"""
        # for observer in self.observers:
        #     observer.update(self)

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        self.temp = temp
        self.humidity = humidity
        self.pressure = pressure

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for observer_one in self.observers:
            observer_one.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weather_data):
        self.temerature = 0
        self.humidity = 0
        self.pressure = 0
        self.weather_data = weather_data # save the ref in an attribute.
        weather_data.registerObserver(self) # register the observer
                                           # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temerature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("\nCurrent conditions:", self.temerature,
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)

# TODO: implement StatisticsDisplay class and ForecastDisplay class.
class StatisticsDisplay(Observer):
    def __init__(self, weather_data):
        self.temparatures = []
        self.humidities = []
        self.pressures = []
        self.weather_data = weather_data # save the ref in an attribute.
        weather_data.registerObserver(self) # register the observer
                                           # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temparatures.append(temperature)
        self.humidities.append(humidity)
        self.pressures.append(pressure)
        self.display()

    def display(self):
        print("\n##########Updated ForecastDisplay:##########",
                "\n\t\tMIN\tMAX\tAVG"
                "\nTemperatures:\t", min(self.temparatures), "\t", max(self.temparatures), "\t", sum(self.temparatures)/len(self.temparatures),
                "\nHumidity:\t", min(self.humidities), "\t", max(self.humidities), "\t", sum(self.humidities)/len(self.humidities),
                "\nPressure:\t", min(self.pressures), "\t", max(self.pressures), "\t", sum(self.pressures)/len(self.pressures)
            )



class ForecastDisplay(Observer):
    def __init__(self, weather_data):
        self.forcast_temp = 0
        self.forcast_humidity = 0
        self.forcast_pressure = 0
        self.weather_data = weather_data # save the ref in an attribute.
        weather_data.registerObserver(self) # register the observer
                                           # so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forcast_humadity = humidity - 0.9 * humidity
        self.forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        self.display()

    def display(self):
        print("\n##########Updated ForecastDisplay:##########",
                "\nTemperature:", self.forcast_temp,
                "\nHumidity:", self.forcast_humidity,
                "\nPressure:", self.forcast_pressure,)

class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)


        weather_data.setMeasurements(80, 65,30.4)
        print("")
        weather_data.setMeasurements(82, 70,29.2)
        print("")
        weather_data.setMeasurements(78, 90,29.2)
        print("")
        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)

        weather_data.removeObserver(forecast_display)
        weather_data.removeObserver(statistics_display)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
