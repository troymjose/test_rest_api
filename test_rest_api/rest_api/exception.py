from test_rest_api.utils.exception import TestRestApiException


class RestApiCreationException(TestRestApiException):
    """
    Exception raised while creating rest api object using RestApi class
    """

    def __init__(self, *, msg: str):
        self.exc = msg
        self.error_msg = """
Rest api creation failed

Example Code
------------
(Example 1)
from test_rest_api import RestApi
my_api = RestApi(
                url = "https://www.MyDomain.com/",
                parameters = { "param1" : "val1", "param2" : "val2" },
                headers = { "Content-Type" : "application/json" },
                body = {}
                )

Note: Only "url" is mandatory and rest are optional
Default parameters: {}
Default headers: {}
Default body: {}
"""
        self.message = self.format(exc=self.exc, error_msg=self.error_msg)
        super().__init__(self.message)


class RestApiSendException(TestRestApiException):
    """
    Exception raised while sending rest api using aiohttp
    """

    def __init__(self, *, msg: str):
        self.exc = msg
        self.error_msg = f"""
Rest api request failed

Example Code
------------
(Example 1)
from my_api_file import my_api
response = await my_api.send(method='get')

(Example 2)
from my_api_file import my_api
response = await my_api.send(method=my_api.METHODS.GET)

(Example 3)
from my_api_file import my_api
response = await my_api.get()

All the above example codes does the same functionality but different with syntax
Supported methods: 'get', 'post', 'put', 'patch', 'delete', 'head', 'options'
"""
        self.message = self.format(exc=self.exc, error_msg=self.error_msg)
        super().__init__(self.message)
