"""

setUp and tearDown is used when we dont want to repeat ourself

setUp will run its code before everys ingle method and tear down will run its code after every single method,
it means whenever any test method is run, first the setup is run and then the main test and finally teardown

setUp class and tearDown class is something which is run before any class and afetr every class

"""

import unittest
from unit_testing import employee

from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = employee.Employee('Karan', 'Shekhawat', 1000)
        self.assertEqual(emp1.email, 'Karan.Shekhawat@email.com')

        emp1.first = 'komal'
        self.assertEqual(emp1.email, 'komal.Shekhawat@email.com')

    def test_fullname(self):
        emp1 = employee.Employee('Karan', 'Shekhawat', 1000)
        self.assertEqual(emp1.fullname, 'Karan Shekhawat')

        emp1.first = 'komal'
        self.assertEqual(emp1.fullname, 'komal Shekhawat')

    def test_apply_raise(self):
        emp1 = employee.Employee('Karan', 'Shekhawat', 1000)
        emp1.apply_raise()
        self.assertEqual(emp1.pay, 1050)


class TestEmployeeSecond(unittest.TestCase):

    def setUp(self):
        self.emp1 = employee.Employee('Karan', 'Shekhawat', 1000)

    def tearDown(self):
        """use it to delete some files that you have created"""
        pass

    def test_email(self):
        self.assertEqual(self.emp1.email, 'Karan.Shekhawat@email.com')

        self.emp1.first = 'komal'
        self.assertEqual(self.emp1.email, 'komal.Shekhawat@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp1.fullname, 'Karan Shekhawat')

        self.emp1.first = 'komal'
        self.assertEqual(self.emp1.fullname, 'komal Shekhawat')

    def test_apply_raise(self):
        self.emp1.apply_raise()
        self.assertEqual(self.emp1.pay, 1050)


class TestMocking(unittest.TestCase):

    def setUp(self):
        self.emp1 = employee.Employee('Karan', 'Shekhawat', 1000)

    def test_monthly_schedule(self):
        with patch('employee.request.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp1.monthly_schedule('MaY')
            mocked_get.assert_called_with('http://company.com/Shekhawat/MaY')
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False
            schedule = self.emp1.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Shekhawat/June')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
