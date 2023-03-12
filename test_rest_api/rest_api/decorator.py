from test_rest_api.rest_api.exception import RestApiConfigException
from test_rest_api.rest_api.rest_api import RestApi


def rest_api(func):
    """
    Decorate your rest api functions.
    Return the rest api config json containing rest api building parameters

    Example:

        @rest_api
        def login_api(username: str, password: str):
            return {
                    url: "https://my_domain.com/login",
                    parameters: {'param1': 'value1', 'param2': 'value2'},
                    headers: {'content-type': 'application/json'},
                    body: {'name':username,'pass':password}
                    }
    """

    def inner(*args, **kwargs) -> RestApi:
        # Get the function name
        name = func.__name__
        # Get the python file path of the function
        module = func.__module__
        # Call the function to retrieve user specified rest api data/config
        rest_api_config: dict = func(*args, **kwargs)
        # Validate if the rest_api_config is a valid dictionary
        if not isinstance(rest_api_config, dict):
            raise RestApiConfigException(name=name, module=module, config=rest_api_config)
        try:
            # Create & return RestApi object
            return RestApi(**rest_api_config)
        except Exception as e:
            raise RestApiConfigException(name=name, module=module, config=rest_api_config, parent_exception=str(e))

    return inner
