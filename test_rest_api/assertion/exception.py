from ..settings import Settings
from ..utils.exception import TestRestApiException


class AssertException(TestRestApiException):
    """
    Exception raised for error in using Assert class
    """

    def __init__(self, *, msg: str):
        self.msg = self.format(msg=msg, doc=Settings.docs.assertion)
        super().__init__(self.msg)
