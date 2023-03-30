from dotenv import dotenv_values
from dataclasses import dataclass
from test_rest_api.global_variables.exception import VariableNotFoundException, ConstantSetException


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
            raise VariableNotFoundException(name=name)

    @classmethod
    def get(cls, name):
        """
        Get the global variable value
        """
        variable_obj = cls._get_variable_obj(name=name)
        return variable_obj.value

    @classmethod
    def set(cls, name, value, is_constant: bool = False):
        """
        Set the global variable value
        """
        try:
            variable_obj = cls._get_variable_obj(name=name)
            # Constants cannot be updated
            if variable_obj.is_constant:
                raise ConstantSetException(name=name)
        except ConstantSetException as exc:
            raise exc
        except Exception as exc:
            pass
        # Set the class attribute
        setattr(cls, name, Variable(value=value, is_constant=is_constant))
