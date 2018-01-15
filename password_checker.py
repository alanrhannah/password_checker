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
        return self.password = self.confirm_password

    def check_string_length(self, length=None):
        """
        Check the length of the string against the rule set.

        Keyword Arguments:
           length {number} -- [The required length of the password]
           (default: {None})
        """
        pass

    def check_lowercase(self, instances_lowercase=None):
        """
        Check if the password strings contains the minimum required
        instance of lowercase charachters.

        Keyword Arguments:
            instances_lowercase {number} -- [The required number of
            lowercase instances] (default: {None})
        """
        pass

    def check_uppercase(self, instances_uppercase=None):
        """
        Check if the password strings contains the minimum required
        instance of lowercase charachters.

        Keyword arguments:
            instances_uppercase {number} -- [The required number of
            lowercase instances] (default: {None})
        """
        pass

    def check_digits(self, instances_digits=None):
        """
        Check if the password strings contains the minimum required
        instance of digits.

        Keyword arguments:
            instances_digits {number} -- [The required number of
            digit instances] (default: {None})
        """
        pass

    def main(self):
        return all(self.check_strings_match(),
                   self.check_string_length(length=8),
                   self.check_lowercase(instances_lowercase=1),
                   self.check_uppercase(instances_uppercase=1),
                   self.check_digits(instances_digits=1))
