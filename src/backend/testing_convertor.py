import pytest
from convertor import convert

# Test cases for conversion
def test_length_conversion():
    assert convert(1, "kilometer", "meter") == 1000, "1 kilometer should equal 1000 meters"
    assert convert(1, "meter", "centimeter") == 100, "1 meter should equal 100 centimeters"

def test_mass_conversion():
    assert convert(1, "kilogram", "gram") == 1000, "1 kilogram should equal 1000 grams"
    assert convert(1, "pound", "ounce") == 16, "1 pound should equal 16 ounces"

def test_temperature_conversion():
    assert round(convert(100, "celsius", "fahrenheit"), 2) == 212, "100 Celsius should equal 212 Fahrenheit"
    assert round(convert(32, "fahrenheit", "celsius"), 2) == 0, "32 Fahrenheit should equal 0 Celsius"

def test_volume_conversion():
    assert convert(1, "liter", "milliliter") == 1000, "1 liter should equal 1000 milliliters"
    assert round(convert(1, "gallon", "liter"), 2) == 3.79, "1 gallon should approximately equal 3.79 liters"

def test_invalid_conversion():
    with pytest.raises(ValueError):
        convert(1, "invalid_unit", "meter")

    with pytest.raises(ValueError):
        convert(1, "meter", "invalid_unit")

# Run the tests if this script is executed directly
if __name__ == "__main__":
    pytest.main()
