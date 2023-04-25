from ..utils.exception import TestRestApiException
from ..settings import Settings


class GlobalVariablesException(TestRestApiException):
    """
    Exception raised for error in using GlobalVariables class
    """

    def __init__(self, *, msg: str):
        self.msg = self.format(msg=msg, doc=Settings.docs.global_variables)
        super().__init__(self.msg)
