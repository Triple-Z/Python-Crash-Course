# 11-1
# import unittest
# from C11.city_functions import city_country
#
#
# class CityTestCase(unittest.TestCase):
#
#     def test_city_country(self):
#         output = city_country('santiago', 'chile')
#         self.assertEqual(output, 'Santiago, Chile')
#
# unittest.main()


# 11-2
import unittest
from C11.city_functions import city_country


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        output = city_country('santiago', 'chile')
        self.assertEqual(output, 'Santiago, Chile')

    def test_city_country_population(self):
        output = city_country('santiago', 'chile', 5000000)
        self.assertEqual(output, "Santiago, Chile - population 5000000")

unittest.main()
