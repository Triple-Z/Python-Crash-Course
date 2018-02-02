# 11-3
import unittest
from C11.Employee import Employee


class EmployeeClassTest(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('triple', 'z', 10000)

    def test_give_default_raise(self):
        self.employee.give_raise()

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)

unittest.main()