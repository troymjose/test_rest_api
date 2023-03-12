from dataclasses import dataclass
from aiohttp import ClientResponse
from test_rest_api.utils.aiohttp_session import AioHttpSession
from test_rest_api.utils.error_msg import ErrorMsg
from test_rest_api.rest_api.exception import RestApiSendException


@dataclass(frozen=True)
class RestApiResponse:
    status_code: int
    content_type: str
    body: dict
    headers: dict
    obj: ClientResponse


class RestApi:
    def __init__(self, url: str, parameters: dict = {}, headers: list = {}, body: dict = {}):
        self.url = url
        self.parameters = parameters
        self.headers = headers
        self.body = body
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
            return await getattr(self, method)()
        except Exception as e:
            raise RestApiSendException(parent_exception=str(e))

    async def create_response(self, response: ClientResponse) -> RestApiResponse:
        """
        Create response object from aiohttp response
        """
        # Retrieve the response body
        body = await response.json()
        # Get the other response parameters
        status_code, headers, content_type = response.status, dict(response.headers), response.content_type
        # Return the RestApiResponse instance object
        return RestApiResponse(status_code=status_code,
                               content_type=content_type,
                               body=body,
                               headers=headers,
                               obj=response)

    async def get(self):
        async with self._session.get(url=self.url,
                                     params=self.parameters,
                                     headers=self.headers,
                                     data=self.body) as response:
            return await self.create_response(response=response)

    async def post(self):
        async with self._session.post(url=self.url,
                                      params=self.parameters,
                                      headers=self.headers,
                                      data=self.body) as response:
            return await self.create_response(response=response)

    async def put(self):
        async with self._session.put(url=self.url,
                                     params=self.parameters,
                                     headers=self.headers,
                                     data=self.body) as response:
            return await self.create_response(response=response)

    async def patch(self):
        async with self._session.patch(url=self.url,
                                       params=self.parameters,
                                       headers=self.headers,
                                       data=self.body) as response:
            return await self.create_response(response=response)

    async def delete(self):
        async with self._session.put(url=self.url,
                                     params=self.parameters,
                                     headers=self.headers,
                                     data=self.body) as response:
            return await self.create_response(response=response)

    async def head(self):
        async with self._session.head(url=self.url,
                                      params=self.parameters,
                                      headers=self.headers,
                                      data=self.body) as response:
            return await self.create_response(response=response)

    async def options(self):
        async with self._session.options(url=self.url,
                                         params=self.parameters,
                                         headers=self.headers,
                                         data=self.body) as response:
            return await self.create_response(response=response)
