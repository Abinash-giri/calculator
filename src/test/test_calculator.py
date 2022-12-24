from main import calculator as calc
import unittest
from unittest.mock import patch

class UnittestCalculator(unittest.TestCase):
    ''' This class unit-tests Calculator file '''
    
    def test_user_input(self):
        ''' This test-case tests input values '''
        value = [3, 4]
        expected_value = [3, 4]
        with patch('main.calculator.get_user_inputs', side_effect = expected_value):
            returned_value = calc.get_user_inputs()
        self.assertEqual(returned_value, value[0])


if __name__=="__main__":
    unittest.main()