import operator
import unittest

from password_checker import PasswordChecker

class TestPasswordChecker(unittest.TestCase):

    def test___init__(self):
        pc = PasswordChecker('foo', 'foo')
        self.assertTrue(pc)

    def test___init__type_error(self):
         with self.assertRaises(TypeError):
            pc = PasswordChecker('foo')

    def test_strings_match(self):
        pc = PasswordChecker('foo', 'foo')
        self.assertTrue(pc.check_strings_match())

    def test_strings_dont_match(self):
        pc = PasswordChecker('foo', 'bar')
        self.assertFalse(pc.check_strings_match())

    def test_str_number_instances_bool_length_true(self):
        pc = PasswordChecker('Password123', 'Password123')
        self.assertTrue(
            pc.str_number_instances_bool(r'.', operator.ge, 8)
        )

    def test_str_number_instances_bool_length_false(self):
        pc = PasswordChecker('Pass', 'Pass')
        self.assertFalse(
            pc.str_number_instances_bool(r'\d', operator.ge, 8)
        )

    def test_str_number_instances_bool_lowercase_true(self):
        pc = PasswordChecker('Password123', 'Password123')
        self.assertTrue(
            pc.str_number_instances_bool(r'[a-z]', operator.ge, 1)
        )

    def test_str_number_instances_bool_lowercase_false(self):
        pc = PasswordChecker('PASSWORD123', 'PASSWORD123')
        self.assertFalse(
            pc.str_number_instances_bool(r'[a-z]', operator.ge, 1)
        )

    def test_str_number_instances_bool_uppercase_true(self):
        pc = PasswordChecker('Password123', 'Password123')
        self.assertTrue(
            pc.str_number_instances_bool(r'[A-Z]', operator.ge, 1)
        )

    def test_str_number_instances_bool_uppercase_false(self):
        pc = PasswordChecker('password123', 'password123')
        self.assertFalse(
            pc.str_number_instances_bool(r'[A-Z]', operator.ge, 1)
        )

    def test_str_number_instances_bool_digit_true(self):
        pc = PasswordChecker('Password123', 'Password123')
        self.assertTrue(
            pc.str_number_instances_bool(r'\d', operator.ge, 1)
        )

    def test_str_number_instances_bool_digit_false(self):
        pc = PasswordChecker('PasswordsAreAwesome', 'PasswordsAreAwesome')
        self.assertFalse(
            pc.str_number_instances_bool(r'\d', operator.ge, 1)
        )

    def test_validate_true(self):
        pc = PasswordChecker('Password123', 'Password123')
        self.assertTrue(pc.validate())

    def test_validate_false_length(self):
        pc = PasswordChecker('Pass12', 'Pass12')
        self.assertFalse(pc.validate())

    def test_validate_false_lowercase(self):
        pc = PasswordChecker('PASSWORD123', 'PASSWORD123')
        self.assertFalse(pc.validate())

    def test_validate_false_uppercase(self):
        pc = PasswordChecker('password123', 'password123')
        self.assertFalse(pc.validate())

    def test_validate_false_digit(self):
        pc = PasswordChecker('Password', 'Password')
        self.assertFalse(pc.validate())


if __name__ == '__main__':
    unittest.main()
