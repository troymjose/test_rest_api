import traceback
import functools
from test_rest_api.utils.error_msg import ErrorMsg
from test_rest_api.rest_api.rest_api import RestApi
from test_rest_api.rest_api.exception import RestApiCreationException


def rest_api(func):
    """
    Decorate your rest api functions.
    Return the rest api config json containing rest api building parameters

    Example:

        @rest_api
        def login_api(username: str, password: str) -> dict:
            return {
                    'url': 'https://my_domain.com/login',
                    'parameters': {'param1': 'value1', 'param2': 'value2'},
                    'headers': {'content-type': 'application/json'},
                    'body': {'name':username,'pass':password}
                    }
    """

    @functools.wraps(func)
    def inner(*args, **kwargs) -> RestApi:
        # Get the name & python file path of the function
        name, module = func.__name__, func.__module__
        # Retrieve user specified rest api config
        try:
            rest_api_config: dict = func(*args, **kwargs)
        except Exception as exc:
            raise RestApiCreationException(name=name,
                                           module=module,
                                           parent_exception=str(exc),
                                           traceback=traceback.format_exc())
        # Validate if the rest_api_config is a valid dictionary
        if not isinstance(rest_api_config, dict):
            raise RestApiCreationException(name=name,
                                           module=module,
                                           parent_exception=ErrorMsg.INVALID_REST_API_CONFIG,
                                           traceback='')
        # Create & return RestApi instance object
        try:
            return RestApi(**rest_api_config, name=name, module=module)
        except Exception as exc:
            raise RestApiCreationException(name=name,
                                           module=module,
                                           parent_exception=str(exc),
                                           traceback='')

    return inner
