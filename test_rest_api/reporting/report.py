import os
import pathlib
from typing import List
from datetime import datetime
from dataclasses import dataclass, asdict
from jinja2 import Environment, FileSystemLoader
from test_rest_api.testing.bug import BugPriority


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
    GLOBAL_VARIABLES: str = 'global_variables'
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
    global_variables: int
    unexpected: int


@dataclass
class ReportTestSummary:
    test: ReportTestSummaryTest = ReportTestSummaryTest(status=True, start='', end='', duration=0, tags=())
    tests: ReportTestSummaryTests = ReportTestSummaryTests(total=0, async_tests=0, sync_tests=0, success=0, fail=0,
                                                           error=0, disable=0, skip=0)
    bugs: ReportTestSummaryBugs = ReportTestSummaryBugs(total=0, low=0, minor=0, major=0, critical=0, blocker=0)
    errors: ReportTestSummaryErrors = ReportTestSummaryErrors(total=0, restapi_creation=0, restapi_send=0,
                                                              global_variables=0, unexpected=0)


class Report:
    def __init__(self):
        self.sync_tests: List[ReportTestResult] = []
        self.async_tests: List[ReportTestResult] = []
        self.summary: ReportTestSummary = ReportTestSummary()
        self.template = Report.create_jija2_template()

    def add_test_result(self, test_result: ReportTestResult):
        """
        Add test result details for a single test
        """
        # Add the test result to tests instance variable only if it's not disabled or skipped
        if test_result.status != TestStatus.DISABLE and test_result.status != TestStatus.SKIP:
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
            # pass is converted to success, because 'pass' is a python keyword & hence we can't create dataclass
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
        """
        Save the test report to the disk
        """
        # Render the jinja report template html file
        rendered_html = self.template.render(summary=self.summary,
                                             sync_tests=self.sync_tests,
                                             async_tests=self.async_tests)
        # Create html report file name using current datetime details
        file_name = f"Result {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.html"
        # Save to html file
        with open(os.path.join(path, file_name), 'w') as f:
            f.write(rendered_html)

    @staticmethod
    def create_jija2_template():
        """
        Jinja2 initialisation
        """
        # Template html file name
        report_template_file_name = 'report.html'
        # Create loader with the current script path
        file_system_loader = FileSystemLoader(searchpath=pathlib.Path(__file__).parent.resolve())
        # Create environment using the above loader
        environment = Environment(loader=file_system_loader)
        # Fetch the template file
        template = environment.get_template(report_template_file_name)
        # Return the template object
        return template


report = Report()
