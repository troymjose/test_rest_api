from test_rest_api.utils.exception import TestRestApiException


class RestApiCreationException(TestRestApiException):
    """
    Exception raised while creating rest api object using RestApi class
    """

    def __init__(self, *, msg: str):
        self.exc = msg
        self.error_msg = """
Rest api creation failed
Tip: Refer the example below !

Example Code
from test_rest_api import RestApi
my_api = RestApi(
                url="https://www.MyDomain.com/",
                parameters={"param1":"val1","param2":"val2"},
                headers={"Content-Type": "application/json"},
                body={}
                )

Note: Only "url" is mandatory and rest are optional
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
Tip: Refer the example below !

Example Code (All the below code does the same functionality but different with syntax):

from my_api_file import my_api
response = await my_api.send(method='get')
or
from test_rest_api import RestApi
from my_api_file import my_api
response = await my_api.send(method=RestApi.METHOD.GET)
or
from my_api_file import my_api
response = await my_api.get()

Supported methods: 'get', 'post', 'put', 'patch', 'delete', 'head', 'options'
"""
        self.message = self.format(exc=self.exc, error_msg=self.error_msg)
        super().__init__(self.message)
