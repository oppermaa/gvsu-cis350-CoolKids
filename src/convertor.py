from pint import UnitRegistry

# Initialize the Unit Registry
ureg = UnitRegistry()

# Dictionary to map conversion types to specific functions
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

def convert_units(value, from_unit, to_unit):
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
        # Define the quantity in the from_unit
        quantity = value * ureg(from_unit)
        # Convert the quantity to the to_unit
        converted_quantity = quantity.to(to_unit)
        return converted_quantity.magnitude  # Return only the numeric value
    except Exception as e:
        print(f"Error converting from {from_unit} to {to_unit}: {e}")
        return None

# Test cases for the function
if __name__ == "__main__":
    # Example conversions
    print("Area Conversion: 1 square kilometer to square mile =", convert_units(1, "square_kilometer", "square_mile"))
    print("Data Transfer Rate Conversion: 1000 bits/second to kilobits/second =", convert_units(1000, "bit/second", "kilobit/second"))
    print("Digital Storage Conversion: 1 gigabyte to megabyte =", convert_units(1, "gigabyte", "megabyte"))
    print("Energy Conversion: 1 kilojoule to calorie =", convert_units(1, "kilojoule", "calorie"))
    print("Frequency Conversion: 1 megahertz to hertz =", convert_units(1, "megahertz", "hertz"))
    print("Fuel Economy Conversion: 1 kilometer/liter to mile/gallon =", convert_units(1, "kilometer/liter", "mile/gallon"))
    print("Length Conversion: 1 kilometer to mile =", convert_units(1, "kilometer", "mile"))
    print("Mass Conversion: 1 kilogram to pound =", convert_units(1, "kilogram", "pound"))
    print("Plane Angle Conversion: 1 degree to radian =", convert_units(1, "degree", "radian"))
    print("Pressure Conversion: 1 atm to pascal =", convert_units(1, "atm", "pascal"))
    print("Speed Conversion: 100 kilometer/hour to mile/hour =", convert_units(100, "kilometer/hour", "mile/hour"))
    print("Temperature Conversion: 100 celsius to fahrenheit =", convert_units(100, "celsius", "fahrenheit"))
    print("Time Conversion: 1 day to seconds =", convert_units(1, "day", "second"))
    print("Volume Conversion: 1 gallon to liter =", convert_units(1, "gallon", "liter"))
