from test_rest_api.utils.exception import TestRestApiException


class VariableNotFoundException(TestRestApiException):
    """
    Exception raised for error in getattr(self, variable)
    """

    def __init__(self, *, name):
        self.exc = 'Global variable not found'
        self.error_msg = f'"{name}" is not present in global variables'
        self.message = self.format(exc=self.exc, error_msg=self.error_msg)
        super().__init__(self.message)


class ConstantSetException(TestRestApiException):
    """
    Exception raised for error in updating variable instance object value with 'is_constant' flag as True
    """

    def __init__(self, *, name):
        self.exc = 'Constant global variables cannot be updated'
        self.error_msg = f'"{name}" is a constant global variable'
        self.message = self.format(exc=self.exc, error_msg=self.error_msg)
        super().__init__(self.message)
