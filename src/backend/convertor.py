from pint import UnitRegistry

# Initialize the Unit Registry
ureg = UnitRegistry()

# Dictionary to map conversion types to specific units (for reference or UI purposes, not directly used in conversion)
conversion_types = {
    "Area": ["square_kilometer", "square_meter", "square_centimeter", "square_mile", "square_yard", "square_foot", "square_inch", "hectare", "acre"],
    "Data Transfer Rate": ["bit/second", "kilobit/second", "kilobyte/second", "kibibit/second", "megabit/second", "megabyte/second", "mebibit/second", "gigabit/second", "gigabyte/second", "gibibit/second", "terabit/second", "terabyte/second", "tebibit/second"],
    "Digital Storage": ["bit", "kilobit", "kibibit", "megabit", "mebibit", "gigabit", "gibibit", "terabit", "tebibit", "petabit", "pebibit", "byte", "kilobyte", "kibibyte", "megabyte", "mebibyte", "gigabyte", "gibibyte", "terabyte", "tebibyte", "petabyte", "pebibyte"],
    "Energy": ["joule", "kilojoule", "calorie", "kilocalorie", "watt_hour", "kilowatt_hour", "electronvolt", "british_thermal_unit", "us_therm", "foot_pound"],
    "Frequency": ["hertz", "kilohertz", "megahertz", "gigahertz"],
    "Fuel Economy": ["mile/gallon", "mile/gallon_imperial", "kilometer/liter", "liter/100_kilometer"],
    "Length": ["kilometer", "meter", "centimeter", "millimeter", "micrometer", "nanometer", "mile", "yard", "foot", "inch", "nautical_mile"],
    "Mass": ["ton", "kilogram", "gram", "milligram", "microgram", "imperial_ton", "us_ton", "stone", "pound", "ounce"],
    "Plane Angle": ["arcsecond", "degree", "gradian", "milliradian", "minute", "radian"],
    "Pressure": ["bar", "pascal", "psi", "atm", "torr"],
    "Speed": ["mile/hour", "foot/second", "meter/second", "kilometer/hour", "knot"],
    "Temperature": ["celsius", "fahrenheit", "kelvin"],
    "Time": ["nanosecond", "microsecond", "millisecond", "second", "minute", "hour", "day", "week", "month", "year", "decade", "century", "millennium"],
    "Volume": ["gallon", "quart", "pint", "cup", "fluid_ounce", "tablespoon", "teaspoon", "cubic_meter", "liter", "milliliter"]
}

def convert(value, from_unit, to_unit):
    """
    Converts a value from one unit to another using pint's UnitRegistry.

    Parameters:
    - value (float): the numeric value to convert
    - from_unit (str): the unit to convert from
    - to_unit (str): the unit to convert to

    Returns:
    - float: the converted value
    """
    try:
        # Ensure units are lowercase for compatibility
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()

        # Define the quantity in the from_unit
        quantity = value * ureg(from_unit)
        
        # Convert the quantity to the to_unit
        converted_quantity = quantity.to(to_unit)

        # Return only the numeric value
        return converted_quantity.magnitude
    except Exception as e:
        # Raise an error with detailed information
        raise ValueError(f"Error converting from {from_unit} to {to_unit}: {e}")

# Debugging tests for standalone execution
if __name__ == "__main__":
    test_cases = [
        (1, "square_kilometer", "square_mile"),
        (1000, "bit/second", "kilobit/second"),
        (1, "gigabyte", "megabyte"),
        (1, "kilojoule", "calorie"),
        (1, "megahertz", "hertz"),
        (1, "kilometer/liter", "mile/gallon"),
        (1, "kilometer", "mile"),
        (1, "kilogram", "pound"),
        (1, "degree", "radian"),
        (1, "atm", "pascal"),
        (100, "kilometer/hour", "mile/hour"),
        (100, "celsius", "fahrenheit"),
        (1, "day", "second"),
        (1, "gallon", "liter")
    ]
    
    for value, from_unit, to_unit in test_cases:
        try:
            result = convert(value, from_unit, to_unit)
            print(f"Converted {value} {from_unit} to {to_unit}: {result}")
        except ValueError as e:
            print(e)
