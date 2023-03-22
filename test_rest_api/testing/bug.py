from dataclasses import dataclass


@dataclass
class BugPriority:
    LOW: str = 'low'
    MINOR: str = 'minor'
    MAJOR: str = 'major'
    CRITICAL: str = 'critical'
    BLOCKER: str = 'blocker'


class BugException(Exception):
    """
    Exception raised by testers when testing rest api response.
    """

    def __init__(self, message="", priority=BugPriority.LOW, actual_result="", expected_result="",
                 steps_to_reproduce=""):
        self._no_data_to_display = 'No data to display'
        self.priority = priority
        self.message = f"""
BUG
---------
{message.strip() if message else self._no_data_to_display}

PRIORITY
---------
{priority.strip() if priority else self._no_data_to_display}

ACTUAL RESULT
---------
{actual_result.strip() if actual_result else self._no_data_to_display}

EXPECTED RESULT
---------
{expected_result.strip() if expected_result else self._no_data_to_display}

STEPS TO REPRODUCE
-------------
{steps_to_reproduce.strip() if steps_to_reproduce else self._no_data_to_display}
"""
        super().__init__(self.message)


def bug(message="", priority="", actual_result="", expected_result="", steps_to_reproduce=""):
    """
    Function used by users to raise bug in their test functions
    """
    raise BugException(message=message,
                       priority=priority,
                       actual_result=actual_result,
                       expected_result=expected_result,
                       steps_to_reproduce=steps_to_reproduce)
