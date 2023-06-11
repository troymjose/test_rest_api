from inspect import getframeinfo, stack
from .. import settings
from ..utils.error_msg import ErrorMsg
from ..utils.exception import catch_exc
from .exception import VariableException


class Variable:
    """
    Variable can be used for correlations in tests
    """

    @classmethod
    def _set(cls, *, name: str, value: any) -> None:
        """
        Set the class attribute
        """
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception(ErrorMsg.VARIABLE_NAME_INVALID_DATA_TYPE)
        # Check if name not empty
        if name.strip() == '':
            raise Exception(ErrorMsg.VARIABLE_EMPTY_STRING)
        # Set class level attribute
        setattr(cls, f'_{name}', value)

    @classmethod
    def _get(cls, *, name: str) -> any:
        """
        Get the class attribute
        """
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception(ErrorMsg.VARIABLE_NAME_INVALID_DATA_TYPE)
        if value := getattr(cls, f'_{name}', None):
            return value
        raise Exception(f'{ErrorMsg.TEST_DATA_NOT_FOUND} "{name}"')

    @classmethod
    @catch_exc(test_rest_api_exception=VariableException)
    def get(cls, name: str) -> any:
        """
        Get test data value using the testdata name
        """
        # Get variable obj
        value = cls._get(name=name)
        # Get the caller object to retrieve the caller code
        caller = getframeinfo(stack()[2][0])
        # Get the caller code
        caller_code = caller.code_context[0].strip()
        # Logging
        print(f"""
Get Variable
------------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {caller_code}
 {settings.logging.sub_point} Result {settings.logging.key_val_sep} {caller_code[:caller_code.find('=')]}= {value}
 {settings.logging.sub_point} Data   {settings.logging.key_val_sep} {name} = {value}
 {settings.logging.sub_point} Type   {settings.logging.key_val_sep} Mutable
""")
        # Return the test data value
        return value

    @classmethod
    @catch_exc(test_rest_api_exception=VariableException)
    def set(cls, name: str, value: any) -> None:
        """
        Set the variable value
        """

        # Set the class attribute
        cls._set(name=name, value=value)
        # Get the caller object to retrieve the caller code
        caller = getframeinfo(stack()[2][0])
        # Get the caller code
        caller_code = caller.code_context[0].strip()
        # Logging
        print(f"""
Set Variable
------------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {caller_code}
 {settings.logging.sub_point} Data   {settings.logging.key_val_sep} {name} = {value}
 {settings.logging.sub_point} Type   {settings.logging.key_val_sep} Mutable
""")
