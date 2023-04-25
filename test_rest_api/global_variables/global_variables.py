from dotenv import dotenv_values
from dataclasses import dataclass
from inspect import getframeinfo, stack
from .. import settings
from ..utils.exception import catch_exc
from .exception import GlobalVariablesException


@dataclass
class Variable:
    """
    Class to create variable object
    value: Contains the value of the variable
    is_constant: Flag is set True for constant variables
    """
    value: str
    is_constant: bool


class GlobalVariables:
    """
    Global variables can be used for parameterization and correlation in tests
    """

    @classmethod
    def _set_env_variables(cls, *, path: str):
        """
        Set .env variable as constants
        """
        # Get env file
        env = dotenv_values(path)
        # Create constant global variables
        for name, value in env.items():
            cls.set(name=name, value=value, is_constant=True)

    @classmethod
    def _get_variable_obj(cls, *, name):
        """
        Get the class attribute
        """
        try:
            return getattr(cls, name)
        except Exception as exc:
            raise Exception(f'Global variable "{name}" not found')

    @classmethod
    @catch_exc(test_rest_api_exception=GlobalVariablesException)
    def get(cls, name):
        """
        Get the global variable value
        """
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception('Invalid data type for name. Please provide a valid string')
        # Get variable obj
        variable_obj = cls._get_variable_obj(name=name)
        # Get the caller object to retrieve the caller code
        caller = getframeinfo(stack()[2][0])
        # Get the caller code
        caller_code = caller.code_context[0].strip()
        # Logging
        print(f"""
Get Global Variable
-------------------
 {settings.logging.sub_point} Code {settings.logging.key_val_sep} {caller.code_context[0].strip()}
 {settings.logging.sub_point} Get  {settings.logging.key_val_sep} {name} = {variable_obj.value}
 {settings.logging.sub_point} Data {settings.logging.key_val_sep} {'Constant' if variable_obj.is_constant else 'Changeable'}
""")
        # Return variable obj value
        return variable_obj.value

    @classmethod
    @catch_exc(test_rest_api_exception=GlobalVariablesException)
    def set(cls, name, value, is_constant: bool = False):
        """
        Set the global variable value
        """
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception('Invalid data type for name. Please provide a valid string')
        # Check if name not empty
        if name.strip() == '':
            raise Exception('Empty value for name. Please provide a valid string')
        # Check if is_constant is of type bool
        if not isinstance(is_constant, bool):
            raise Exception('Invalid data type for is_constant. Please provide a valid boolean')
        try:
            variable_obj = cls._get_variable_obj(name=name)
        except Exception as exc:
            variable_obj = None
        # Constants cannot be updated
        if variable_obj and variable_obj.is_constant:
            raise Exception(f'Constant global variable "{name}" cannot be updated')
        # Set the class attribute
        setattr(cls, name, Variable(value=value, is_constant=is_constant))
        # Get the caller object to retrieve the caller code
        caller = getframeinfo(stack()[2][0])
        # Get the caller code
        caller_code = caller.code_context[0].strip()
        # Dont print .env Global Variables Set
        if caller_code.startswith('GlobalVariables.'):
            # Logging
            print(f"""
Set Global Variable
-------------------
 {settings.logging.sub_point} Code {settings.logging.key_val_sep} {caller.code_context[0].strip()}
 {settings.logging.sub_point} Set  {settings.logging.key_val_sep} {name} = {value}
 {settings.logging.sub_point} Data {settings.logging.key_val_sep} {'Constant' if is_constant else 'Changeable'}
""")
