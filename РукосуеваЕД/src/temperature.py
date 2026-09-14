"""Simple temperature conversion utilities used to demonstrate CI."""

ABSOLUTE_ZERO_CELSIUS = -273.15


def celsius_to_fahrenheit(celsius: float) -> float:
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError("Temperature below absolute zero is not possible")
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    celsius = (fahrenheit - 32) * 5 / 9
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError("Temperature below absolute zero is not possible")
    return celsius


def celsius_to_kelvin(celsius: float) -> float:
    if celsius < ABSOLUTE_ZERO_CELSIUS:
        raise ValueError("Temperature below absolute zero is not possible")
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    if kelvin < 0:
        raise ValueError("Temperature in Kelvin cannot be negative")
    return kelvin - 273.15
