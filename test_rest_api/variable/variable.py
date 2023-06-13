from inspect import getframeinfo, stack
from .. import settings
from ..utils.exception import catch_exc
from .exception import VariableException


class Variable:
    """
    Variable can be used for correlations in tests
    """

    @catch_exc(test_rest_api_exception=VariableException)
    def __getattribute__(self, attribute: str) -> any:
        try:
            # Get the class attribute value
            value = super().__getattribute__(attribute)
            # Get the caller object to retrieve the caller code
            caller = getframeinfo(stack()[2][0])
            # Get the caller code
            caller_code = caller.code_context[0].strip()
            # Only log for one condition. Example: my_value = variable.attribute
            if caller_code.strip().endswith(f'.{attribute}'):
                # Logging
                print(f"""
Get Variable
------------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {caller_code}
 {settings.logging.sub_point} Result {settings.logging.key_val_sep} {caller_code[:caller_code.find('=')]}= {value}
 {settings.logging.sub_point} Data   {settings.logging.key_val_sep} {attribute} = {value}
 {settings.logging.sub_point} Type   {settings.logging.key_val_sep} Mutable
""")
            return value
        except Exception as exc:
            raise Exception(exc)

    @catch_exc(test_rest_api_exception=VariableException)
    def __setattr__(self, attr_name: str, attr_value: any):
        try:
            # Set the class attribute
            super().__setattr__(attr_name, attr_value)
            # Get the caller object to retrieve the caller code
            caller = getframeinfo(stack()[2][0])
            # Get the caller code
            caller_code = caller.code_context[0].strip()
            # Only log for one condition. Example: variable.attr_name = attr_value
            if caller_code.strip().replace(' ', '').endswith(f'{attr_name}={attr_value}'):
                # Logging
                print(f"""
Set Variable
------------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {caller_code}
 {settings.logging.sub_point} Data   {settings.logging.key_val_sep} {attr_name} = {attr_value}
 {settings.logging.sub_point} Type   {settings.logging.key_val_sep} Mutable
""")
        except Exception as exc:
            raise Exception(f'Exception: {exc}')


variable = Variable()
