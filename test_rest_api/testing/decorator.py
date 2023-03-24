import re
import traceback
import functools
from datetime import datetime
from inspect import iscoroutinefunction
from test_rest_api.utils.colors import colors
from test_rest_api.testing.bug import BugException
from test_rest_api.utils.logger import test_rest_api_logger
from test_rest_api.reporting.report import report, ReportTestResult, TestStatus, ErrorType
from test_rest_api.rest_api.exception import RestApiCreationException, RestApiSendException


def test(*, name="", desc="", enabled=True, tags=()):
    def testcase_decorator(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            # Get the test file path
            testsuite: str = func.__module__
            # Create the test name
            testcase_name: str = f'{name} ({testsuite})' if name else f'{func.__name__} ({testsuite})'
            # Get the type of test function
            is_async = True if iscoroutinefunction(func) else False
            # Initialise test status and test details
            test_status, test_details = TestStatus.DISABLE, 'Testcase is disabled'
            # Initialise bug priority and error type which will be used for reporting
            bug_priority, error_type = '', ''
            # Set the start time of the test
            start = datetime.now()
            # Only execute enabled testcases
            if enabled:
                # Update the test status and details
                test_status, test_details = TestStatus.SKIP, 'Testcase is skipped'
                try:
                    # Check the type of function (async or sync)
                    if is_async:
                        # Call the async test function
                        await func(*args, **kwargs)
                    else:
                        # Call the sync test function
                        func(*args, **kwargs)
                    # Log the result
                    test_rest_api_logger.info(f"{colors.LIGHT_GREEN}{testcase_name}{colors.LIGHT_CYAN}")
                    # Update the test status and details
                    test_status, test_details = TestStatus.PASS, 'Testcase successfully completed with zero errors'
                except RestApiCreationException as rest_api_creation_exc:
                    # Log the result
                    test_rest_api_logger.info(f"{colors.YELLOW}{testcase_name}{colors.LIGHT_CYAN}")
                    # Update the error type for reporting
                    error_type = ErrorType.RESTAPI_CREATION
                    # Get the code traceback details
                    traceback_data = traceback.format_exc()
                    # Format the traceback (Remove unwanted info)
                    testing_res = re.search(r'test_rest_api/testing/decorator.py", line (.*?), in inner',
                                            traceback_data)
                    rest_api_res = re.search(r'raise RestApiCreationException', traceback_data)
                    traceback_data = traceback_data[testing_res.start() + 89:rest_api_res.end()]
                    traceback_data = traceback_data[:traceback_data.rfind('File "') - 3]
                    # Update the test status and details
                    test_status, test_details = TestStatus.ERROR, f'{traceback_data}\n{rest_api_creation_exc}'
                except RestApiSendException as rest_api_send_exc:
                    # Log the result
                    test_rest_api_logger.info(f"{colors.YELLOW}{testcase_name}{colors.LIGHT_CYAN}")
                    # Update the error type for reporting
                    error_type = ErrorType.RESTAPI_SEND
                    # Get the code traceback details
                    traceback_data = traceback.format_exc()
                    # Format the traceback (Remove unwanted info)
                    testing_res = re.search(r'test_rest_api/testing/decorator.py", line (.*?), in inner',
                                            traceback_data)
                    rest_api_res = re.search(r'raise RestApiSendException', traceback_data)
                    traceback_data = traceback_data[testing_res.start() + 89:rest_api_res.end()]
                    traceback_data = traceback_data[:traceback_data.rfind('File "') - 3]
                    traceback_data = traceback_data[:traceback_data.rfind('File "') - 3]
                    # Update the test status and details
                    test_status, test_details = TestStatus.ERROR, f'{traceback_data}\n{rest_api_send_exc}'
                except BugException as bug_exc:
                    # Log the result
                    test_rest_api_logger.info(f"{colors.LIGHT_RED}{testcase_name}{colors.LIGHT_CYAN}")
                    # Update the bug priority for reporting
                    bug_priority = bug_exc.priority
                    # Get the code traceback details
                    traceback_data = traceback.format_exc()
                    # Format the traceback (Remove unwanted info)
                    testing_res = re.search(r'test_rest_api/testing/decorator.py", line (.*?), in inner',
                                            traceback_data)
                    bug_res = re.search(r'raise BugException', traceback_data)
                    traceback_data = traceback_data[testing_res.start() + 89:bug_res.end()]
                    traceback_data = traceback_data[:traceback_data.rfind('File "') - 3]
                    traceback_data = traceback_data[:traceback_data.rfind('File "') - 3]
                    # Update the test status and details
                    test_status, test_details = TestStatus.FAIL, f'{traceback_data}\n{bug_exc}'
                except Exception as exc:
                    # Log the result
                    test_rest_api_logger.info(f"{colors.YELLOW}{testcase_name}{colors.LIGHT_CYAN}")
                    # Update the error type for reporting
                    error_type = ErrorType.UNEXPECTED
                    # Get the code traceback details
                    traceback_data = traceback.format_exc()
                    # Format the traceback (Remove unwanted info)
                    res = re.search(r'test_rest_api/testing/decorator.py", line (.*?), in inner', traceback_data)
                    traceback_data = traceback_data[res.start() + 89:]
                    # Update the test status and details
                    test_status, test_details = TestStatus.ERROR, f'{traceback_data}\n{exc}'
            # Set the end time of the test
            end = datetime.now()
            # Calculate the time duration of the test
            duration = end - start
            # Create Report test result object instance
            test_result = ReportTestResult(name=testcase_name,
                                           desc=desc,
                                           is_async=is_async,
                                           testsuite=testsuite,
                                           status=test_status,
                                           details=test_details,
                                           tags=tags,
                                           start=start.strftime('%Y-%m-%d %H:%M:%S'),
                                           end=end.strftime('%Y-%m-%d %H:%M:%S'),
                                           duration=str(duration),
                                           bug_priority=bug_priority,
                                           error_type=error_type)
            # Add the test result to the report
            report.add_test_result(test_result)

        # Only async functions can be decorated with @test
        inner.is_testcase = True
        inner.is_async_testcase = True if iscoroutinefunction(func) else False
        return inner

    return testcase_decorator
