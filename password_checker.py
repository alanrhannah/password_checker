import argparse
import getpass
import operator
import re


class PasswordChecker(object):
    """Check password strings for conditions and return boolean value"""
    def __init__(self, password, confirm_password):
        """
        Initiate the PasswordChecker class.

        Checks validity of passwords against the set rules

        Arguments:
            password {string} -- the password string
            confirm_password {string} -- the confirm password string
        """
        self.password = password
        self.confirm_password = confirm_password

    def check_strings_match(self):
        """
        Check the password entry strings match.

        Returns:
            boolean -- a boolean
        """
        return self.password == self.confirm_password

    def str_number_instances_bool(self, regex, operator_rule, num_instances):
        """
        Check occurances of instances of a regex rule matches and return boolen.

        Arguments:
            regex -- [a regex string]
            operator_rule -- [an operator function, i.e. operator.lt]
            num_instances -- [a number of instances required.

        Returns:
            boolean -- a boolean value
        """
        instances_list = re.findall(regex, self.password)

        return operator_rule(len(instances_list), num_instances)


    def validate(self):
        """
        Validate the user input matches the rules as expected.

        Returns:
            boolean -- a boolean value
        """
        match = self.check_strings_match()
        length_boolean = self.str_number_instances_bool(r'.', operator.ge, 8)
        lowercase_boolean = self.str_number_instances_bool(
            r'[a-z]', operator.ge, 1)

        uppercase_boolean = self.str_number_instances_bool(
            r'[A-Z]', operator.ge, 1)

        digit_boolean = self.str_number_instances_bool(
            r'\d', operator.ge, 1)

        return all([match,
                   length_boolean,
                   lowercase_boolean,
                   uppercase_boolean,
                   digit_boolean])


if __name__ == "__main__":
    user_input_password = getpass.getpass('Please Enter Password: ')
    user_input_confirm_password = getpass.getpass('Please Confirm Password: ')

    password_checker = PasswordChecker(user_input_password,
                                       user_input_confirm_password)

    print 'Password Valid: {}'.format(password_checker.validate())
