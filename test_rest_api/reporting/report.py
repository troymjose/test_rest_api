from typing import Dict
from dataclasses import dataclass, asdict

from test_rest_api import BugPriority


@dataclass
class TestStatus:
    PASS: str = 'pass'
    FAIL: str = 'fail'
    ERROR: str = 'error'
    DISABLE: str = 'disable'
    SKIP: str = 'skip'


@dataclass
class ErrorType:
    RESTAPI_CREATION: str = 'restapi_creation'
    RESTAPI_SEND: str = 'restapi_send'
    UNEXPECTED: str = 'unexpected'


@dataclass
class ReportTestResult:
    name: str
    desc: str
    testsuite: str
    status: str
    details: str
    tags: tuple
    start: str
    end: str
    duration: str
    bug_priority: str
    error_type: str


@dataclass
class ReportTestSummaryTest:
    start: str
    end: str
    duration: str
    tags: tuple
    status: bool


@dataclass
class ReportTestSummaryTests:
    total: int
    success: int
    fail: int
    error: int
    disable: int
    skip: int


@dataclass
class ReportTestSummaryBugs:
    total: int
    low: int
    minor: int
    major: int
    critical: int
    blocker: int


@dataclass
class ReportTestSummaryErrors:
    total: int
    restapi_creation: int
    restapi_send: int
    unexpected: int


@dataclass
class ReportTestSummary:
    test: ReportTestSummaryTest = ReportTestSummaryTest(status=True, start='', end='', duration=0, tags=())
    tests: ReportTestSummaryTests = ReportTestSummaryTests(total=0, success=0, fail=0, error=0, disable=0, skip=0)
    bugs: ReportTestSummaryBugs = ReportTestSummaryBugs(total=0, low=0, minor=0, major=0, critical=0, blocker=0)
    errors: ReportTestSummaryErrors = ReportTestSummaryErrors(total=0, restapi_creation=0, restapi_send=0, unexpected=0)


class Report:
    def __init__(self):
        self.tests: Dict[str:ReportTestResult] = {}
        self.summary: ReportTestSummary = ReportTestSummary()

    def add_test_result(self, test_result: ReportTestResult):
        # Add the test result to tests instance variable
        self.tests[test_result.name] = test_result
        # Update the total tests count
        self.summary.tests.total += 1
        # Update the overall test summary status if failed (It was initialized as True)
        if test_result.status == TestStatus.FAIL or test_result.status == TestStatus.ERROR:
            self.summary.test.status = False
        # Update the total test status count
        if test_result.status in asdict(TestStatus()).values():
            setattr(self.summary.tests, test_result.status,
                    getattr(self.summary.tests, test_result.status) + 1)
        # Update the total bug and bug priority count
        if test_result.status == TestStatus.FAIL and test_result.bug_priority in asdict(BugPriority()).values():
            self.summary.bugs.total += 1
            setattr(self.summary.bugs, test_result.bug_priority,
                    getattr(self.summary.bugs, test_result.bug_priority) + 1)
        # Update the total error and error type count
        if test_result.status == TestStatus.ERROR and test_result.error_type in asdict(ErrorType()).values():
            self.summary.errors.total += 1
            setattr(self.summary.errors, test_result.error_type,
                    getattr(self.summary.errors, test_result.error_type) + 1)


report = Report()
