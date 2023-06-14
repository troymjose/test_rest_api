import os
import sys
import json
from ..utils.error_msg import ErrorMsg
from ..utils.exception import catch_exc
from .exception import TestDataException
from ..variable.variable import Variable
from ..utils.string_color import str_color
from ..utils.logger import test_rest_api_logger


class TestData(Variable):
    """
    Test data can be used for parameterization in tests
    """

    class Meta:
        data_type: str = 'Immutable'

    @catch_exc(test_rest_api_exception=TestDataException)
    def __getattribute__(self, attribute: str) -> any:
        return super().__getattribute__(attribute)

    @catch_exc(test_rest_api_exception=TestDataException)
    def __setattr__(self, attr_name: str, attr_value: any):
        raise Exception(ErrorMsg.TEST_DATA_RUNTIME_SET)

    def _set(self, *, path: str) -> None:
        """
        Set test data from file/folder path. Supported file extensions: josn
        """
        # Logging
        test_rest_api_logger.info(str_color.info('Auto detecting test data files'))
        # Set test data from json files
        self._set_from_json_files(path=path)

    def _set_from_json_files(self, *, path: str) -> None:
        """
        Set test data from json files
        """
        # Initialise json_file_paths list to store all the auto fetched json file paths
        self.__dict__['json_file_paths'] = []
        # Auto detect json file paths
        self._get_json_file_paths(path=path)
        # Return if test data json file path list is empty
        if not self.json_file_paths:
            return
        # Logging
        test_rest_api_logger.info(str_color.info(f'Configuring test data from json files'))
        try:
            # Total test data count
            test_data_count = 0
            # Iterate through each json file path
            for file in self.json_file_paths:
                # Open json file
                with open(file) as f:
                    # Load Json data
                    data = json.load(f)
                    # Count the total keys in this file & update the total count
                    test_data_count += len(data)
                    # Iterating through the json data
                    for name, value in data.items():
                        # Set test data attribute
                        self._set_attr(name=name, value=value)
        except Exception as exc:
            sys.exit(str_color.exception(f'{exc}\nFile : {os.path.basename(file)}\nPath : {file}'))
        # Logging
        test_rest_api_logger.info(
            str_color.info(
                f'Initialised {test_data_count} test data variables from {len(self.json_file_paths)} json files'))

    def _get_json_file_paths(self, *, path: str) -> None:
        """
        Auto-detect json files from a test data folder/file path to a list
        Files can be under any nested folder
        """
        if path.endswith("__pycache__") or path.endswith('.py'):
            return
        if os.path.isfile(path) and path.endswith('.json'):
            self.json_file_paths.append(path)
        elif os.path.isdir(path):
            for nested_path in os.listdir(path):
                self._get_json_file_paths(path=path + "/" + nested_path)

    def _set_attr(self, *, name: str, value: any) -> None:
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
        try:
            if value := getattr(self, name):
                raise Exception(f'{ErrorMsg.TEST_DATA_DUPLICATE}{input_details}')
        except Exception as exc:
            pass
        # Set class level attribute
        # Call the base version of __setattr__ you avoid the infinite recursive error
        super().__setattr__(name, value)


testdata = TestData()
