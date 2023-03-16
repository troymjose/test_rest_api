import functools
import logging
from inspect import iscoroutinefunction
from test_rest_api.utils.colors import colors
from test_rest_api.testing.bug import BugException
from test_rest_api.reporting.report import report, ReportItem, test_status


def test(*, name="", desc="", enabled=True, testdata=(), tags=()):
    def testcase_decorator(func):
        @functools.wraps(func)
        async def inner(*args, **kwargs):
            testsuite: str = func.__module__
            testcase_name: str = f'{name} ({testsuite})' if name else f'{func.__name__} ({testsuite})'
            testcase_status: str = test_status.SKIP
            report_item = ReportItem(name=testcase_name,
                                     desc=desc,
                                     status=testcase_status,
                                     testdata=testdata,
                                     tags=tags,
                                     logs=[],
                                     )
            # report._add(report_item=report_item)
            if enabled:
                try:
                    await func(*args, **kwargs)
                    logging.info(f"{colors.LIGHT_GREEN}{testcase_name}{colors.LIGHT_CYAN}")
                    testcase_status: str = test_status.PASS
                except BugException as bug_exc:
                    logging.info(f"{colors.LIGHT_RED}{testcase_name} - {bug_exc.message}{colors.LIGHT_CYAN}")
                    testcase_status: str = test_status.FAIL
                except Exception as exc:
                    logging.info(f"{colors.YELLOW}{testcase_name}{colors.LIGHT_CYAN}")
                    testcase_status: str = test_status.ERROR
            else:
                testcase_status: str = test_status.DISABLED

            report.tests[testcase_name].status = testcase_status

        # Only async functions can be decorated with @test
        inner.is_testcase = True if iscoroutinefunction(func) else False
        return inner

    return testcase_decorator
