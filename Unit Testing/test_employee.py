import unittest
from sched import scheduler
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self) -> None:
        self.emp_1 = Employee('Alin', 'Stefan', 5000)
        self.emp_2 = Employee('Madalina', 'Luiza', 6000)

    def tearDown(self) -> None:
        print('tearDown\n')

    def test_email(self):

        self.assertEqual(self.emp_1.email, 'Alin.Stefan@email.com')
        self.assertEqual(self.emp_2.email, 'Madalina.Luiza@email.com')# add assertion here

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.email, 'John.Stefan@email.com')
        self.assertEqual(self.emp_2.email, 'Jane.Luiza@email.com')

    def test_fullname(self):


        self.assertEqual(self.emp_1.fullname, 'Alin Stefan')
        self.assertEqual(self.emp_2.fullname, 'Madalina Luiza')

        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Stefan')
        self.assertEqual(self.emp_2.fullname, 'Jane Luiza')

    def test_apply_raise(self):


        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 5250)
        self.assertEqual(self.emp_2.pay, 6300)

    def test_monthly_scheduled(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Stefan/May')
            self.assertEqual(schedule, 'Success')
if __name__ == '__main__':
    unittest.main()
