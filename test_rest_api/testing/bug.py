class BugException(Exception):
    """
    Exception raised by testers when testing rest api response.
    """

    def __init__(self, message="", priority="", actual_result="", expected_result="", steps_to_reproduce=""):
        self.message: str = message
        self.priority: str = priority
        self.actual_result: str = actual_result
        self.expected_result: str = expected_result
        self.steps_to_reproduce: str = steps_to_reproduce
        super().__init__(self.message)


class BugPriority:
    LOW: str = 'low'
    MINOR: str = 'minor'
    MAJOR: str = 'major'
    CRITICAL: str = 'critical'
    BLOCKER: str = 'blocker'


def bug(message="", priority="", actual_result="", expected_result="", steps_to_reproduce=""):
    raise BugException(message=message,
                       priority=priority,
                       actual_result=actual_result,
                       expected_result=expected_result,
                       steps_to_reproduce=steps_to_reproduce)
