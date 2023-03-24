import re
from test_rest_api.utils.error_msg import ErrorMsg


class RestApiException(Exception):
    """
    Base Exception class
    """
    _no_data_to_display = 'No data to display'

    @staticmethod
    def format_traceback(traceback: str, search: str, extra_len: int) -> str:
        """
        Remove the data provided above the rest api file, to make the traceback more readable
        """
        if not traceback:
            return ''
        res = re.search(search, traceback)
        if not res:
            return traceback
        return traceback[res.start() + extra_len:]


class RestApiCreationException(RestApiException):
    """
    Exception raised while creating rest api object form json data returned form @rest_api decorated functions
    """

    def __init__(self, *, name: str, module: str, parent_exception: str, traceback: str):
        self.message = f"""
EXCEPTION
---------
{parent_exception.strip() if parent_exception else self._no_data_to_display}

FILE NAME
---------
{name.strip() if name else self._no_data_to_display}

FILE PATH
---------
{module.strip() if module else self._no_data_to_display}

TRACEBACK
---------
{self.format_traceback(traceback=traceback, search=r'test_rest_api/test_rest_api/rest_api/decorator.py", line (.*?), in inner', extra_len=122).strip() if traceback else self._no_data_to_display}

ERROR MESSAGE
-------------
{ErrorMsg.INVALID_REST_API.strip()}
"""
        super().__init__(self.message)


class RestApiSendException(RestApiException):
    """
    Exception raised while sending rest api using aiohttp
    """

    def __init__(self, *, name: str, module: str, parent_exception: str, traceback: str):
        self.message = f"""
EXCEPTION
---------
{parent_exception.strip() if parent_exception else self._no_data_to_display}

FILE NAME
---------
{name.strip() if name else self._no_data_to_display}

FILE PATH
---------
{module.strip() if module else self._no_data_to_display}

TRACEBACK
---------
{self.format_traceback(traceback=traceback, search=r'test_rest_api/test_rest_api/rest_api/rest_api.py", line (.*?), in', extra_len=130).strip() if traceback else self._no_data_to_display}

ERROR MESSAGE
-------------
{ErrorMsg.REST_API_SEND_EXCEPTION.strip()}
"""
        super().__init__(self.message)
