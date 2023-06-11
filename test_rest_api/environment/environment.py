import os
import sys
from dotenv import dotenv_values
from inspect import getframeinfo, stack
from .. import settings
from ..utils.error_msg import ErrorMsg
from ..utils.exception import catch_exc
from ..utils.string_color import str_color
from .exception import EnvironmentException
from ..utils.logger import test_rest_api_logger


class Environment:
    """
    Used for parameterization in rest api creation
    """

    @classmethod
    def _set_from_env_file(cls, *, path: str):
        """
        Set environment variables from .env file
        """
        # Return if path is empty or None
        if not path:
            return
        # Logging
        test_rest_api_logger.info(str_color.info(f'Configuring environment from .env file'))
        try:
            # Get env file
            env = dotenv_values(path)
            # Create constant global variables
            for name, value in env.items():
                # Set environment
                cls._set(name=name, value=value)
        except Exception as exc:
            sys.exit(str_color.exception(f'{exc}\nFile : {os.path.basename(path)}\nPath : {path}'))
        # Logging
        test_rest_api_logger.info(str_color.info(f'Initialised {len(env)} environment values from .env file'))

    @classmethod
    def _set(cls, *, name: str, value: any) -> None:
        """
        Set the class attribute
        """
        # String representation of name & value for exception messages
        input_details = f'\nName : {name}\nValue: {value}'
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception(f'{ErrorMsg.ENVIRONMENT_INVALID_DATA_TYPE}{input_details}')
        # Check if name not empty
        if name.strip() == '':
            raise Exception(f'{ErrorMsg.ENVIRONMENT_EMPTY_STRING}{input_details}')
        # Check for duplicates
        if getattr(cls, f'_{name}', None):
            raise Exception(f'{ErrorMsg.ENVIRONMENT_DUPLICATE}{input_details}')
        # Set class level attribute
        setattr(cls, f'_{name}', value)

    @classmethod
    def _get(cls, *, name: str) -> str:
        """
        Get the class attribute
        """
        if value := getattr(cls, f'_{name}', None):
            return value
        raise Exception(f'{ErrorMsg.ENVIRONMENT_NOT_FOUND} "{name}"')

    @classmethod
    @catch_exc(test_rest_api_exception=EnvironmentException)
    def get(cls, name: str) -> any:
        """
        Get environment value using the name
        """
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception(ErrorMsg.ENVIRONMENT_NAME_INVALID_DATA_TYPE)
        # Get variable obj
        value = cls._get(name=name)
        # Get the caller object to retrieve the caller code
        caller = getframeinfo(stack()[2][0])
        # Get the caller code
        caller_code = caller.code_context[0].strip()
        # Logging
        print(f"""
Get Environment Variable
-------------------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {caller_code}
 {settings.logging.sub_point} Result {settings.logging.key_val_sep} {caller_code[:caller_code.find('=')]}= {value}
 {settings.logging.sub_point} Data   {settings.logging.key_val_sep} {name} = {value}
 {settings.logging.sub_point} Type   {settings.logging.key_val_sep} Immutable
""")
        # Return the test data value
        return value
