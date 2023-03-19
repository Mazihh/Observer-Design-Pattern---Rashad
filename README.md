# Observer-Design-Pattern---Rashad

In this example, we have implemented the Observer pattern using a simple example of a weather station. The Observable class maintains a list of observers and provides methods to add and remove observers, as well as a notify_observers method that calls the update method on each observer with any arguments provided.

The Observer class defines a simple interface that all observers must implement. In this case, we have two concrete observers: TemperatureDisplay and TemperatureLogger. The WeatherStation class is an observable that has a set_temperature method that notifies all observers of a change in temperature.

By using the Observer pattern, we can decouple the WeatherStation class from its observers, making it more flexible and easier to maintain.
