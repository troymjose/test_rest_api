from .. import settings
from ..utils.exception import TestRestApiException


class RestApiCreationException(TestRestApiException):
    """
    Exception raised while creating rest api object using RestApi class
    """

    def __init__(self, *, msg: str):
        self.msg = self.format(msg=msg, doc=settings.docs.rest_api_creation)
        super().__init__(self.msg)


class RestApiSendException(TestRestApiException):
    """
    Exception raised while sending rest api using aiohttp
    """

    def __init__(self, *, msg: str):
        self.msg = self.format(msg=msg, doc=settings.docs.rest_api_send)
        super().__init__(self.msg)
