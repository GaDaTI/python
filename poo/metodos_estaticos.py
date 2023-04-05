""" INTRODUÇÃO AOS METODOS ESTÁTICOS """

class TemperatureConverter:
    kevin = 'K'
    farenheit = 'F'
    celsius = 'C'

    @staticmethod
    def celsius_to_fahrenheit(value_celsius):
        return 9*value_celsius/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(value_fahrenheit):
        return 5 * (value_fahrenheit - 32)/9

    @staticmethod
    def celsius_to_kelvin(value_celsius):
        return value_celsius + 273.15

    @staticmethod
    def kelvin_to_celssius(value_kelvin):
        return value_kelvin + 273.15

    @staticmethod
    def fahrenheit_to_kelvin(value_fahrenheit):
        return 5 * (value_fahrenheit + 459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(value_kelvin):
        return 9 * value_kelvin/5 - 459.67

    @staticmethod
    def  format(value, unit):
        symbol = ' '
        if unit == TemperatureConverter.farenheit:
            symbol = ' ºF '
        elif unit == TemperatureConverter.celsius:
            symbol = ' ºC'
        elif unit == TemperatureConverter.kevin:
            symbol = 'ºK'

        return f'{value} {symbol}'


if __name__ == '__main__' :
    new_york = TemperatureConverter.celsius_to_fahrenheit(35)
    print(TemperatureConverter.format(new_york, TemperatureConverter.farenheit))


