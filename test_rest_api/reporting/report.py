import os
import json
from typing import List
from datetime import datetime
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
    is_async: bool
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
    sync_tests: int
    async_tests: int
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
    tests: ReportTestSummaryTests = ReportTestSummaryTests(total=0, async_tests=0, sync_tests=0, success=0, fail=0,
                                                           error=0, disable=0, skip=0)
    bugs: ReportTestSummaryBugs = ReportTestSummaryBugs(total=0, low=0, minor=0, major=0, critical=0, blocker=0)
    errors: ReportTestSummaryErrors = ReportTestSummaryErrors(total=0, restapi_creation=0, restapi_send=0, unexpected=0)


class Report:
    def __init__(self):
        self.sync_tests: List[ReportTestResult] = []
        self.async_tests: List[ReportTestResult] = []
        self.summary: ReportTestSummary = ReportTestSummary()

    def add_test_result(self, test_result: ReportTestResult):
        # Add the test result to tests instance variable
        if test_result.status != TestStatus.DISABLE:
            if test_result.is_async:
                self.async_tests.append(test_result)
            else:
                self.sync_tests.append(test_result)
        # Update the total tests count
        self.summary.tests.total += 1
        # Update the sync and async tests count
        if test_result.is_async:
            self.summary.tests.async_tests += 1
        else:
            self.summary.tests.sync_tests += 1
        # Update the overall test summary status if failed (It was initialized as True)
        if test_result.status == TestStatus.FAIL or test_result.status == TestStatus.ERROR:
            self.summary.test.status = False
        # Update the total test status count
        if test_result.status in asdict(TestStatus()).values():
            test_result.status = 'success' if test_result.status == TestStatus.PASS else test_result.status
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

    def save(self, *, path):
        # Initialise result dictionary
        result = {}
        # Update the result dictionary
        result['summary'] = asdict(self.summary)
        result['sync_tests'] = [asdict(test) for test in self.sync_tests]
        result['async_tests'] = [asdict(test) for test in self.async_tests]
        # Save to json file
        file_name = f"Result {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}.json"
        with open(os.path.join(path, file_name), 'w') as f:
            json.dump(result, f)


report = Report()
