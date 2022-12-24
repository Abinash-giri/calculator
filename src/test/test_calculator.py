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


    def test_check_user_interest_true(self):
        '''This test-case tests true user-interests'''
        with patch('builtins.input', return_value = 'y'):
            self.assertTrue(calc.check_user_interest())

    
    def test_check_user_interest_false(self):
        '''This test-case tests false user-interests'''
        with patch('builtins.input', return_value = 'n'):
            self.assertFalse(calc.check_user_interest())

    
    def test_check_user_interest_invalid(self):
        '''This test-case tests invalid user-interests'''
        with patch('builtins.input', return_value = 'c'):
            self.assertFalse(calc.check_user_interest())

    
    def test_perform_operation_minvalue(self):
        '''This testcase tests minimun values for operation'''
        self.assertEqual(None, calc.perform_operation(1, [22]))


    def test_perform_operation_2_add(self):
        '''This testcase tests add 2 values'''
        self.assertEqual(None, calc.perform_operation(1, [2, 3]))

    
    def test_perform_operation_2_sub(self):
        '''This testcase tests sub 2 values'''
        self.assertEqual(None, calc.perform_operation(2, [6, 3]))


    def test_perform_operation_2_mul(self):
        '''This testcase tests mul 2 values'''
        self.assertEqual(None, calc.perform_operation(3, [6, 3]))

    
    def test_perform_operation_2_sub(self):
        '''This testcase tests div 2 values'''
        self.assertEqual(None, calc.perform_operation(4, [6, 3]))


    def test_perform_operation_more2_add(self):
        '''This testcase tests add more than 2 values'''
        self.assertEqual(None, calc.perform_operation(1, [6, 3, 1, 5]))

    
    def test_perform_operation_more2_sub(self):
        '''This testcase tests sub more than 2 values'''
        self.assertEqual(None, calc.perform_operation(2, [21, 3, 1, 5]))


    def test_perform_operation_more2_mul(self):
        '''This testcase tests mul more than 2 values'''
        self.assertEqual(None, calc.perform_operation(3, [6, 3, 1, 5]))

    
    def test_perform_operation_more2_div(self):
        '''This testcase tests div more than 2 values'''
        self.assertEqual(None, calc.perform_operation(4, [6, 3, 2]))


    def test_start_calculator_valid_True(self):
        ''' This testcase tests valid true response'''
        choice_dict = {1 : "Addition", 2 : "Substraction", 3 : "Multiplication" ,\
                   4 : "Division"}
        with patch('builtins.input', return_value = 1):
            with patch('main.calculator.get_user_inputs', return_value = [1,2,3,4]):
                with patch('main.calculator.perform_operation', return_value = None):
                    with patch('main.calculator.check_user_interest', return_value = True):
                        self.assertTrue(calc.start_calculator(choice_dict))


    def test_start_calculator_valid_False(self):
        ''' This testcase tests valid true response'''
        choice_dict = {1 : "Addition", 2 : "Substraction", 3 : "Multiplication" ,\
                   4 : "Division"}
        with patch('builtins.input', return_value = 1):
            with patch('main.calculator.get_user_inputs', return_value = [1,2,3,4]):
                with patch('main.calculator.perform_operation', return_value = None):
                    with patch('main.calculator.check_user_interest', return_value = False):
                        self.assertFalse(calc.start_calculator(choice_dict))