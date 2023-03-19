class Observable:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)

class Observer:
    def update(self, *args, **kwargs):
        pass

class WeatherStation(Observable):
    def set_temperature(self, temperature):
        self.notify_observers(temperature=temperature)

class TemperatureDisplay(Observer):
    def update(self, *args, **kwargs):
        temperature = kwargs.get('temperature')
        print(f"The temperature is {temperature} degrees Celsius.")

class TemperatureLogger(Observer):
    def update(self, *args, **kwargs):
        temperature = kwargs.get('temperature')
        # write the temperature to a log file or database

# Example usage:
weather_station = WeatherStation()
temperature_display = TemperatureDisplay()
temperature_logger = TemperatureLogger()

weather_station.add_observer(temperature_display)
weather_station.add_observer(temperature_logger)

weather_station.set_temperature(25.5)
# Output: "The temperature is 25.5 degrees Celsius."

weather_station.remove_observer(temperature_display)

weather_station.set_temperature(26.0)
# The temperature will be logged, but not displayed since the display observer was removed.