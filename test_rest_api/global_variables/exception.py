from .. import settings
from ..utils.exception import TestRestApiException


class GlobalVariablesException(TestRestApiException):
    """
    Exception raised for error in using GlobalVariables class
    """

    def __init__(self, *, msg: str):
        self.msg = self.format(msg=msg, doc=settings.docs.global_variables)
        super().__init__(self.msg)
