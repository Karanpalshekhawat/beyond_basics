import unittest
from unit_testing import employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp1 = employee.Employee('Karan', 'Shekhawat', 1000)
        self.assertEqual(emp1.email, 'Karan.Shekhawat@email.com')

        emp1.first = 'komal'
        self.assertEqual(emp1.email, 'komal.Shekhawat@email.com')

if __name__ == '__main__':
    unittest.main()
