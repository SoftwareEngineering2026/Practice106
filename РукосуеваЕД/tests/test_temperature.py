import pytest

from src.temperature import (
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0


def test_celsius_below_absolute_zero_raises():
    with pytest.raises(ValueError):
        celsius_to_fahrenheit(-300)


def test_kelvin_negative_raises():
    with pytest.raises(ValueError):
        kelvin_to_celsius(-1)
