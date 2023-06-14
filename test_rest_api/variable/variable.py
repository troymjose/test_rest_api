import re
from inspect import getframeinfo, stack
from .. import settings
from ..utils.exception import catch_exc
from .exception import VariableException


class Variable:
    """
    Variable can be used for correlations in tests
    """

    class Meta:
        data_type: str = 'Mutable'

    _get_stack_index = lambda self: 2 if type(self).__name__ == 'Variable' else 4
    _create_title = lambda self: " ".join(re.findall("[A-Z][^A-Z]*", self.__class__.__name__))

    @catch_exc(test_rest_api_exception=VariableException)
    def __getattribute__(self, attribute: str) -> any:
        try:
            # Get the class attribute value
            # Call the base version of __getattribute__ you avoid the infinite recursive error
            value = super().__getattribute__(attribute)
            # Select stack by checking if it is called form base class or inherited class
            stack_array_index = self._get_stack_index()
            # Get the caller object to retrieve the caller code
            caller = getframeinfo(stack()[stack_array_index][0])
            # Get the caller code
            caller_code = caller.code_context[0].strip()
            # Only log for one condition. Example: my_value = variable.attribute
            if caller_code.endswith(f'.{attribute}'):
                # Logging
                self.log(title=f'Get {self._create_title()}',
                         code=caller_code,
                         result=f"{caller_code[:caller_code.find('=')]}= {value}",
                         data=f"{attribute} = {value}", )
            return value
        except Exception as exc:
            raise Exception(exc)

    @catch_exc(test_rest_api_exception=VariableException)
    def __setattr__(self, attr_name: str, attr_value: any):
        try:
            # Set the class attribute
            # Call the base version of __setattr__ you avoid the infinite recursive error
            super().__setattr__(attr_name, attr_value)
            # Select stack by checking if it is called form base class or inherited class
            stack_array_index = self._get_stack_index()
            # Get the caller object to retrieve the caller code
            caller = getframeinfo(stack()[stack_array_index][0])
            # Get the caller code
            caller_code = caller.code_context[0].strip()
            # Only log for one condition. Example: variable.attr_name = attr_value
            if caller_code.strip().replace(' ', '').endswith(f'{attr_name}={attr_value}'):
                # Logging
                self.log(title=f'Set {self._create_title()}',
                         code=caller_code,
                         result=f'Value set to {attr_value}',
                         data=f"{attr_name} = {attr_value}", )
        except Exception as exc:
            raise Exception(f'Exception: {exc}')

    def log(self, title: str, code: str, result: str, data: str) -> None:
        print(f"""
{title}
------------
{settings.logging.sub_point} Code   {settings.logging.key_val_sep} {code}
{settings.logging.sub_point} Result {settings.logging.key_val_sep} {result}
{settings.logging.sub_point} Data   {settings.logging.key_val_sep} {data}
{settings.logging.sub_point} Type   {settings.logging.key_val_sep} {self.Meta.data_type}
""")


variable = Variable()
