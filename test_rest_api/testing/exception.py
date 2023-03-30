from test_rest_api.utils.exception import TestRestApiException


class BugCreationException(TestRestApiException):
    """
    Exception raised while creating bug object using Bug class
    """

    def __init__(self, *, msg: str):
        self.exc = msg
        self.error_msg = """
Bug creation failed
Tip: Refer the example below !

Example Code
from test_rest_api import Bug
Bug(message="my bug msg",
    priority=Bug.PRIORITY.CRITICAL,
    actual_result="my actual result",
    expected_result="my expected result",
    steps_to_reproduce="detailed steps to reproduce")

Note: All the arguments are optional.

from test_rest_api import Bug
Bug()

Default bug priority: 'low'
Supported bug priorities: 'low', 'minor', 'major', 'critical', 'blocker'
"""
        self.message = self.format(exc=self.exc, error_msg=self.error_msg)
        super().__init__(self.message)
