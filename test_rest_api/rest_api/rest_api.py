import traceback
from dataclasses import dataclass
from aiohttp import ClientResponse
from aiohttp.client_exceptions import ClientConnectorError, InvalidURL, ContentTypeError
from test_rest_api.utils.error_msg import ErrorMsg
from test_rest_api.utils.aiohttp_session import AioHttpSession
from test_rest_api.rest_api.exception import RestApiSendException


class RestApiMethod:
    GET: str = 'get'
    POST: str = 'post'
    PUT: str = 'put'
    PATCH: str = 'patch'
    DELETE: str = 'delete'
    HEAD: str = 'head'
    OPTIONS: str = 'options'


@dataclass(frozen=True)
class RestApiResponse:
    status_code: int
    content_type: str
    body: dict
    headers: dict
    obj: ClientResponse


class RestApi:
    def __init__(self, name: str, module: str, url: str, parameters: dict = {}, headers: list = {}, body: dict = {}):
        # Rest api variables
        self.url = url
        self.parameters = parameters
        self.headers = headers
        self.body = body
        # File variables
        self.name = name
        self.module = module
        # Aiohttp variables
        self._session = AioHttpSession()

    async def send(self, method: str):
        """
        Send the rest api by providing the request method
        """
        try:
            # Convert to lowercase
            method = method.lower()
            # Check if the method is valid
            if method not in {'get', 'post', 'put', 'patch', 'delete', 'head', 'options'}:
                raise Exception(ErrorMsg.INVALID_METHOD)
            # Send the request
            async with getattr(self._session, method)(url=self.url,
                                                      params=self.parameters,
                                                      headers=self.headers,
                                                      data=self.body) as response:
                return await self._create_response(response=response)
        except ClientConnectorError as exc:
            raise RestApiSendException(name=self.name, module=self.module, parent_exception=str(exc),
                                       traceback=traceback.format_exc())
        except InvalidURL as exc:
            raise RestApiSendException(name=self.name, module=self.module, parent_exception='Invalid ULR',
                                       traceback=traceback.format_exc())
        except ContentTypeError as exc:
            raise RestApiSendException(name=self.name, module=self.module, parent_exception=str(exc),
                                       traceback=traceback.format_exc())
        except Exception as exc:
            raise RestApiSendException(name=self.name, module=self.module, parent_exception=str(exc),
                                       traceback=traceback.format_exc())

    async def _create_response(self, response: ClientResponse) -> RestApiResponse:
        """
        Create response instance object from aiohttp async response
        """
        # Retrieve the response body in JSON
        body = await response.json()
        # Get the other response parameters
        status_code, headers, content_type = response.status, dict(response.headers), response.content_type
        # Create and return the RestApiResponse instance object
        return RestApiResponse(status_code=status_code,
                               content_type=content_type,
                               body=body,
                               headers=headers,
                               obj=response)

    async def get(self):
        """
        Send HTTP GET Request
        """
        return await self.send(method=RestApiMethod.GET)

    async def post(self):
        """
        Send HTTP POST Request
        """
        return await self.send(method=RestApiMethod.POST)

    async def put(self):
        """
        Send HTTP PUT Request
        """
        return await self.send(method=RestApiMethod.PUT)

    async def patch(self):
        """
        Send HTTP PATCH Request
        """
        return await self.send(method=RestApiMethod.PATCH)

    async def delete(self):
        """
        Send HTTP DELETE Request
        """
        return await self.send(method=RestApiMethod.DELETE)

    async def head(self):
        """
        Send HTTP HEAD Request
        """
        return await self.send(method=RestApiMethod.HEAD)

    async def options(self):
        """
        Send HTTP OPTIONS Request
        """
        return await self.send(method=RestApiMethod.OPTIONS)
