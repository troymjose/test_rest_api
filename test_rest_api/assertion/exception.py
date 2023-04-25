from .. import settings
from ..utils.exception import TestRestApiException


class AssertException(TestRestApiException):
    """
    Exception raised for error in using Assert class
    """

    def __init__(self, *, msg: str):
        self.msg = self.format(msg=msg, doc=settings.docs.assertion)
        super().__init__(self.msg)
