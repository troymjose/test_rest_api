from dataclasses import dataclass


@dataclass
class TestResult:
    name: str
    desc: str
    status: bool
    logs: list


class Report:
    """

    """

    def __init__(self):
        self.tests = {}

    def add_test_result(self, test_result: TestResult):
        self.tests[test_result.name] = test_result
