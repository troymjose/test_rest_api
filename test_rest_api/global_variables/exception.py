class VariableNotFoundException(Exception):
    """
    Exception raised for error in getattr(self, variable)
    """

    def __init__(self, *, name):
        self.message = f"""
EXCEPTION
---------
Global variable not found

ERROR MESSAGE
-------------
'{name}' is not present in global variables
"""
        super().__init__(self.message)


class ConstantSetException(Exception):
    """
    Exception raised for error in updating variable instance object value with 'is_constant' flag as True
    """

    def __init__(self, *, name):
        self.message = f"""
EXCEPTION
---------
Constant global variables cannot be updated

ERROR MESSAGE
-------------
'{name}' is a constant global variable
"""
        super().__init__(self.message)
