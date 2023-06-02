import os
import sys
import json
from inspect import getframeinfo, stack
from .. import settings
from ..utils.error_msg import ErrorMsg
from ..utils.exception import catch_exc
from .exception import TestDataException
from ..utils.string_color import str_color
from ..utils.logger import test_rest_api_logger


class TestData:
    """
    Test data can be used for parameterization in tests
    """

    @classmethod
    def _set_from_json_files(cls, *, files: str) -> None:
        """
        Set test data from json files
        """
        # Return if test data files list is empty
        if not files:
            return
        # Logging
        test_rest_api_logger.info(str_color.info(f'Configuring test data from json files'))
        try:
            # Total test data count
            test_data_count = 0
            for file in files:
                # Open json file
                with open(file) as f:
                    # Load Json data
                    data = json.load(f)
                    # Count the total keys in this file & update the total count
                    test_data_count += len(data)
                    # Iterating through the json data
                    for name, value in data.items():
                        # Set the attribute in TestData
                        cls._set(name=name, value=value)
        except Exception as exc:
            sys.exit(str_color.exception(f'{exc}\nFile : {os.path.basename(file)}\nPath : {file}'))
        # Logging
        test_rest_api_logger.info(
            str_color.info(f'Initialised {test_data_count} test data variables from {len(files)} json files'))

    @classmethod
    def _set(cls, *, name: str, value: any) -> None:
        """
        Set the class attribute
        """
        # String representation of name & value for exception messages
        input_details = f'\nKey  : {name}\nValue: {value}'
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception(f'{ErrorMsg.TEST_DATA_INVALID_DATA_TYPE}{input_details}')
        # Check if name not empty
        if name.strip() == '':
            raise Exception(f'{ErrorMsg.TEST_DATA_EMPTY_STRING}{input_details}')
        # Check for duplicates
        if getattr(cls, f'_{name}', None):
            raise Exception(f'{ErrorMsg.TEST_DATA_DUPLICATE}{input_details}')
        # Set class level attribute
        setattr(cls, f'_{name}', value)

    @classmethod
    def _get(cls, *, name: str) -> any:
        """
        Get the class attribute
        """
        if value := getattr(cls, f'_{name}', None):
            return value
        raise Exception(f'{ErrorMsg.TEST_DATA_NOT_FOUND} "{name}"')

    @classmethod
    @catch_exc(test_rest_api_exception=TestDataException)
    def get(cls, name: str) -> any:
        """
        Get test data value using the testdata name
        """
        # Check if name is of type string
        if not isinstance(name, str):
            raise Exception(ErrorMsg.TEST_DATA_NAME_INVALID_DATA_TYPE)
        # Get variable obj
        value = cls._get(name=name)
        # Get the caller object to retrieve the caller code
        caller = getframeinfo(stack()[2][0])
        # Get the caller code
        caller_code = caller.code_context[0].strip()
        # Logging
        print(f"""
Get Test Data
-------------------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {caller_code}
 {settings.logging.sub_point} Result {settings.logging.key_val_sep} {caller_code[:caller_code.find('=')]} = {value}
 {settings.logging.sub_point} Data   {settings.logging.key_val_sep} {name} = {value}
 {settings.logging.sub_point} Type   {settings.logging.key_val_sep} Immutable
""")
        # Return the test data value
        return value
