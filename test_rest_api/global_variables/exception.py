class VariableNotFoundException(Exception):
    """
    Exception raised for error in getattr(self, variable)
    """

    def __init__(self, *, name):
        self.message = f"Variable not found.\n'{name}' is not present in global variables"
        super().__init__(self.message)


class ConstantSetException(Exception):
    """
    Exception raised for error in updating variable instance object value with 'is_constant' flag as True
    """

    def __init__(self, *, name):
        self.message = f"Constant global variables cannot be updated.\n'{name}' is a constant global variable"
        super().__init__(self.message)
