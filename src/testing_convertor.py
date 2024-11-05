import unittest
from convertor import convert_units

class TestConvertor(unittest.TestCase):
    
    # Testing Area conversions
    def test_square_kilometer_to_square_mile(self):
        result = convert_units(1, "square_kilometer", "square_mile")
        self.assertAlmostEqual(result, 0.386102, places=5)

    def test_square_meter_to_square_foot(self):
        result = convert_units(1, "square_meter", "square_foot")
        self.assertAlmostEqual(result, 10.7639, places=4)

    # Testing Data Transfer Rate conversions
    def test_bit_per_second_to_kilobit_per_second(self):
        result = convert_units(1000, "bit/second", "kilobit/second")
        self.assertAlmostEqual(result, 1, places=2)

    def test_megabyte_per_second_to_gigabit_per_second(self):
        result = convert_units(1, "megabyte/second", "gigabit/second")
        self.assertAlmostEqual(result, 0.008, places=3)

    # Testing Digital Storage conversions
    def test_byte_to_kilobyte(self):
        result = convert_units(1024, "byte", "kilobyte")
        self.assertEqual(result, 1)

    def test_gigabyte_to_megabyte(self):
        result = convert_units(1, "gigabyte", "megabyte")
        self.assertEqual(result, 1024)

    # Testing Energy conversions
    def test_joule_to_calorie(self):
        result = convert_units(4184, "joule", "calorie")
        self.assertAlmostEqual(result, 1000, places=0)

    def test_kilocalorie_to_joule(self):
        result = convert_units(1, "kilocalorie", "joule")
        self.assertAlmostEqual(result, 4184, places=0)

    # Testing Frequency conversions
    def test_hertz_to_kilohertz(self):
        result = convert_units(1000, "hertz", "kilohertz")
        self.assertEqual(result, 1)

    # Testing Fuel Economy conversions
    def test_mpg_to_kpl(self):
        result = convert_units(10, "mile/gallon", "kilometer/liter")
        self.assertAlmostEqual(result, 4.25144, places=5)

    # Testing Length conversions
    def test_meter_to_centimeter(self):
        result = convert_units(1, "meter", "centimeter")
        self.assertEqual(result, 100)

    def test_kilometer_to_mile(self):
        result = convert_units(1, "kilometer", "mile")
        self.assertAlmostEqual(result, 0.621371, places=5)

    # Testing Mass conversions
    def test_kilogram_to_pound(self):
        result = convert_units(1, "kilogram", "pound")
        self.assertAlmostEqual(result, 2.20462, places=5)

    def test_gram_to_milligram(self):
        result = convert_units(1, "gram", "milligram")
        self.assertEqual(result, 1000)

    # Testing Plane Angle conversions
    def test_degree_to_radian(self):
        result = convert_units(180, "degree", "radian")
        self.assertAlmostEqual(result, 3.14159, places=5)

    # Testing Pressure conversions
    def test_atm_to_pascal(self):
        result = convert_units(1, "atm", "pascal")
        self.assertAlmostEqual(result, 101325, places=0)

    # Testing Speed conversions
    def test_kph_to_mph(self):
        result = convert_units(100, "kilometer/hour", "mile/hour")
        self.assertAlmostEqual(result, 62.1371, places=4)

    # Testing Temperature conversions
    def test_celsius_to_fahrenheit(self):
        result = convert_units(100, "celsius", "fahrenheit")
        self.assertEqual(result, 212)

    def test_fahrenheit_to_kelvin(self):
        result = convert_units(32, "fahrenheit", "kelvin")
        self.assertAlmostEqual(result, 273.15, places=2)

    # Testing Time conversions
    def test_hour_to_second(self):
        result = convert_units(1, "hour", "second")
        self.assertEqual(result, 3600)

    def test_minute_to_millisecond(self):
        result = convert_units(1, "minute", "millisecond")
        self.assertEqual(result, 60000)

    # Testing Volume conversions
    def test_liter_to_milliliter(self):
        result = convert_units(1, "liter", "milliliter")
        self.assertEqual(result, 1000)

    def test_gallon_to_liter(self):
        result = convert_units(1, "gallon", "liter")
        self.assertAlmostEqual(result, 3.78541, places=5)

if __name__ == "__main__":
    unittest.main()
# Wait for the convertor.py file
