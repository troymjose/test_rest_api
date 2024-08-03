import os
from typing import List, Dict
from datetime import datetime
from jinja2 import Environment
from dataclasses import dataclass, asdict, field
from .html import html_str
from ..bug.bug import BugPriority
from ..settings.logging import logging


@dataclass
class TestStatus:
    """ Dataclass to store test status """
    PASS: str = 'pass'
    FAIL: str = 'fail'
    ERROR: str = 'error'
    DISABLE: str = 'disable'
    SKIP: str = 'skip'


@dataclass
class ErrorType:
    """ Dataclass to store error types """
    BUG: str = 'bug'
    REST_API: str = 'rest_api'
    VARIABLE: str = 'variable'
    CONSTANT: str = 'constant'
    TEST_DATA: str = 'test_data'
    ASSERTION: str = 'assertion'
    UNEXPECTED: str = 'unexpected'
    ENVIRONMENT: str = 'environment'


@dataclass
class ReportTestResult:
    """ Testcase result, contains all the details of a single testcase """
    name: str
    desc: str
    asyncio_task: str
    is_async: bool
    testsuite: str
    status: str
    details: str
    tags: str
    start: str
    end: str
    duration: str
    bug_priority: str
    error_type: str


@dataclass
class ReportTestSummaryTest:
    """ Generic details of the test run """
    start: str = ''
    end: str = ''
    duration: str = ''
    tags: tuple = ()
    status: bool = True
    total: int = 0
    environment_variables: int = 0
    testdata_variables: int = 0
    testdata_files: int = 0
    logs: int = 0
    assertions: int = 0
    requests: int = 0
    responses: int = 0

    def __str__(self):
        """ String representation of the test run details """
        return f"""
{logging.console_report} Total Tests Executed ({self.total})
{logging.console_report} Run Status : {'PASS' if self.status else 'FAIL'}
{logging.console_report} Tags       : {'#' + ' #'.join(self.tags) if self.tags else '#ALL'}
{logging.console_report} Start Time : {self.start}
{logging.console_report} End Time   : {self.end}
{logging.console_report} Duration   : {self.duration}
"""


@dataclass
class ReportTestSummaryTests:
    """ Details of the test run status counts """
    total: int = 0
    sync_tests: int = 0
    async_tests: int = 0
    success: int = 0
    fail: int = 0
    error: int = 0
    disable: int = 0
    skip: int = 0

    def __str__(self):
        """ String representation of the test run status counts """
        return f"""
{logging.console_report} Total Tests ({self.sync_tests} sync + {self.async_tests} async = {self.total} tests)
{logging.console_report} Success : {self.success}
{logging.console_report} Fail    : {self.fail}
{logging.console_report} Error   : {self.error}
{logging.console_report} Disable : {self.disable}
{logging.console_report} Skip    : {self.skip}
"""


@dataclass
class ReportTestSummaryBugs:
    """ Details of the test run bug counts """
    total: int = 0
    low: int = 0
    minor: int = 0
    major: int = 0
    critical: int = 0
    blocker: int = 0

    def __str__(self):
        """ String representation of the test run bug counts """
        # If total bugs is 0, then return empty string
        if self.total == 0:
            return ''
        return f"""
{logging.console_report} Total Bugs ({self.total})
{logging.console_report} Low      : {self.low}
{logging.console_report} Minor    : {self.minor}
{logging.console_report} Major    : {self.major}
{logging.console_report} Critical : {self.critical}
{logging.console_report} Blocker  : {self.blocker}
"""


@dataclass
class ReportTestSummaryErrors:
    """ Details of the test run error counts """
    total: int = 0
    bug: int = 0
    rest_api: int = 0
    variable: int = 0
    constant: int = 0
    test_data: int = 0
    assertion: int = 0
    unexpected: int = 0
    environment: int = 0

    def __str__(self):
        """ String representation of the test error counts """
        # If total errors is 0, then return empty string
        if self.total == 0:
            return ''
        return f"""
{logging.console_report} Total Errors ({self.total})
{logging.console_report} Bug         : {self.bug}
{logging.console_report} Rest API    : {self.rest_api}
{logging.console_report} Variable    : {self.variable}
{logging.console_report} Constant    : {self.constant}
{logging.console_report} Test Data   : {self.test_data}
{logging.console_report} Assertion   : {self.assertion}
{logging.console_report} Unexpected  : {self.unexpected}
{logging.console_report} Environment : {self.environment}
"""


@dataclass
class ReportTestSummary:
    """ Test summary, contains all the details of the whole test run """
    test: ReportTestSummaryTest = field(default_factory=lambda: ReportTestSummaryTest())
    tests: ReportTestSummaryTests = field(default_factory=lambda: ReportTestSummaryTests())
    bugs: ReportTestSummaryBugs = field(default_factory=lambda: ReportTestSummaryBugs())
    errors: ReportTestSummaryErrors = field(default_factory=lambda: ReportTestSummaryErrors())

    def __str__(self):
        """ String representation of the test summary """
        return f'{self.test}{self.tests}{self.bugs}{self.errors}'


@dataclass
class ReportTestExtras:
    """ Test extras, contains all the details which cannot be filled at decorator level. Uses asyncio_task as key """
    logs: dict = field(default_factory=lambda: {})
    assertions: dict = field(default_factory=lambda: {})
    requests: dict = field(default_factory=lambda: {})
    responses: dict = field(default_factory=lambda: {})


class Report:
    """ Handles the test rest api report """

    def __init__(self):
        """ Initialize the test report """
        # Stores the synchronous test results
        self.sync_tests: List[ReportTestResult] = []
        # Stores the asynchronous test results
        self.async_tests: List[ReportTestResult] = []
        # Stores the test results in a dictionary with testcase name as key
        self.tests: Dict[str:ReportTestResult] = {}
        # Stores the test summary details
        self.summary: ReportTestSummary = ReportTestSummary()
        # Stores the test extras details which cannot be filled at decorator level using asyncio_task as key
        self.extras: ReportTestExtras = ReportTestExtras()

    def add_test_result(self, test_result: ReportTestResult):
        """ Add test result details for a single testcase """
        # Update the total count of tests to be displayed in test status details section
        self.summary.tests.total += 1
        # Update the sync and async tests count to be displayed in sync async donut section
        if test_result.is_async:
            self.summary.tests.async_tests += 1
        else:
            self.summary.tests.sync_tests += 1
        # Add the test result to tests instance variable only if it's not disabled or skipped
        if test_result.status not in [TestStatus.DISABLE, TestStatus.SKIP]:
            # Update the total test run count, This will not include the disabled or skipped tests
            self.summary.test.total += 1
            # Add to the respective sync or async tests list
            if test_result.is_async:
                self.async_tests.append(test_result)
            else:
                self.sync_tests.append(test_result)
        # Update the test run status to failed if any of the test fails or errors out
        if test_result.status in [TestStatus.FAIL, TestStatus.ERROR]:
            self.summary.test.status = False
        # Update the total test status count
        if test_result.status in asdict(TestStatus()).values():
            # pass is converted to success, because 'pass' is a python keyword & hence we can't create dataclass
            # This change is done for handling ReportTestSummaryTests dataclass which uses "success" instead of "pass"
            report_test_summary_tests_status = 'success' if test_result.status == TestStatus.PASS else test_result.status
            # Dynamically set test status counts by adding 1 to the current status count
            setattr(self.summary.tests, report_test_summary_tests_status,
                    getattr(self.summary.tests, report_test_summary_tests_status) + 1)
        # Update the total bug and bug priority count
        if test_result.status == TestStatus.FAIL and test_result.bug_priority in asdict(BugPriority()).values():
            # Update the total bug count
            self.summary.bugs.total += 1
            # Dynamically set bug priority counts by adding 1 to the current bug priority count
            setattr(self.summary.bugs, test_result.bug_priority,
                    getattr(self.summary.bugs, test_result.bug_priority) + 1)
        # Update the total error and error type count
        if test_result.status == TestStatus.ERROR and test_result.error_type in asdict(ErrorType()).values():
            # Update the total error count
            self.summary.errors.total += 1
            # Dynamically set error type counts by adding 1 to the current error type count
            setattr(self.summary.errors, test_result.error_type,
                    getattr(self.summary.errors, test_result.error_type) + 1)

    def add_message_to_logs(self, *, asyncio_task, message):
        """ Add log details to report extras logs dictionary using asyncio_task as key for each test """
        # If asyncio_task is not present in logs, then create a key with asyncio_task and assign empty string
        if asyncio_task not in self.extras.logs:
            self.extras.logs[asyncio_task] = ''
        # Append the message to the existing log message
        self.extras.logs[asyncio_task] += message
        # Increment the total log count by 1, test run level
        self.summary.test.logs += 1

    def update_extras_assertions(self, *, asyncio_task):
        """ Add assertion count details to report extras assertions dict using asyncio_task as key for each test """
        # If asyncio_task is not present in assertions, then create a key with asyncio_task and assign 0
        if asyncio_task not in self.extras.assertions:
            self.extras.assertions[asyncio_task] = 0
        # Increment the assertion count by 1, test level
        self.extras.assertions[asyncio_task] += 1
        # Increment the total assertion count by 1, test run level
        self.summary.test.assertions += 1

    def update_extras_requests(self, *, asyncio_task):
        """ Add request count details to report extras requests dict using asyncio_task as key for each test """
        # If asyncio_task is not present in requests, then create a key with asyncio_task and assign 0
        if asyncio_task not in self.extras.requests:
            self.extras.requests[asyncio_task] = 0
        # Increment the request count by 1, test level
        self.extras.requests[asyncio_task] += 1
        # Increment the total request count by 1, test run level
        self.summary.test.requests += 1

    def update_extras_responses(self, *, asyncio_task):
        """ Add response count details to report extras responses dict using asyncio_task as key for each test """
        # If asyncio_task is not present in responses, then create a key with asyncio_task and assign 0
        if asyncio_task not in self.extras.responses:
            self.extras.responses[asyncio_task] = 0
        # Increment the response count by 1, test level
        self.extras.responses[asyncio_task] += 1
        # Increment the total response count by 1, test run level
        self.summary.test.responses += 1

    def save(self, *, path):
        """ Save the test report to a html file """
        # Create Jinja2 template
        template = self._create_jija2_template()
        # Render the jinja report template html file
        rendered_html = template.render(summary=self.summary,
                                        sync_tests=self.sync_tests,
                                        async_tests=self.async_tests,
                                        extras=self.extras)
        # Create html report file name using current datetime details
        file_name = f"Result {datetime.now().strftime('%Y-%m-%d %H-%M-%S')}.html"
        # Save to html file to the path and ensure utf-8 encoding
        with open(os.path.join(path, file_name), 'w', encoding="utf-8") as f:
            f.write(rendered_html)

    @staticmethod
    def _create_jija2_template():
        """ Jinja2 initialisation """
        # Create Jinja environment
        environment = Environment()
        # Create Jinja template
        template = environment.from_string(html_str)
        # Return the template object
        return template


# Create a report object to be used throughout the test execution
report = Report()
