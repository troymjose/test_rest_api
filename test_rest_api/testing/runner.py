import os
import sys
import json
import traceback
import types
import aiohttp
import asyncio
import importlib.machinery
from datetime import datetime
from time import perf_counter_ns
from inspect import getmembers, iscoroutinefunction
from ..reporting.report import report
from ..utils.error_msg import ErrorMsg
from ..utils.string_color import str_color
from ..utils.logger import test_rest_api_logger
from ..utils.aiohttp_session import AioHttpSession


class Runner:
    """
    Execute all test cases
    Auto detect test suites and test cases
    """

    def __init__(self):
        # Test suite path
        self.test_suite_path: str = ''
        # Test result path
        self.test_result_path: str = ''
        # Test tags
        self.test_tags: list = []
        # List of file paths
        self.test_files: list = []
        # List of @test decorated sync function objects
        self.sync_tests: list = []
        # List of @test decorated async function objects
        self.async_tests: list = []

    def load_module(self, file: str):
        """
        Load the module in runtime and return it
        """
        # Create module path from file path
        name = file.replace(self.test_suite_path, '').replace('/', '.')[1:-3]
        # Load the module
        loader = importlib.machinery.SourceFileLoader(name, file)
        module = types.ModuleType(name)
        loader.exec_module(module)
        # Return the module
        return module

    def load_test_file_sync_tests(self, mod):
        """
        From test file load all the @test decorated sync function objects in a list
        Conditions: Is sync Function & Decorated with @test
        """
        return [obj for _, obj in getmembers(mod) if
                iscoroutinefunction(obj) and obj.__dict__.get('is_testcase', False) and not obj.__dict__.get(
                    'is_async_testcase', False)]

    def load_test_file_async_tests(self, mod):
        """
        From test file load all the @test decorated async function objects in a list
        Conditions: Is Async Function & Decorated with @test
        """
        return [obj for _, obj in getmembers(mod) if
                iscoroutinefunction(obj) and obj.__dict__.get('is_testcase', False) and obj.__dict__.get(
                    'is_async_testcase', False)]

    def load_tests(self):
        """
        Auto-detect @test decorated sync and async functions from the list of test python files
        Update the function objects in tests list
        """
        # For each file path in list of python files from testsuite folder
        for test_file in self.test_files:
            # Load the module in runtime from file paths
            module = self.load_module(test_file)
            # Load the @test decorated sync functions as a list from the module
            sync_tests = self.load_test_file_sync_tests(module)
            # Update the sync_tests instance variable
            self.sync_tests.extend(sync_tests)
            # Load the @test decorated async functions as a list from the module
            async_tests = self.load_test_file_async_tests(module)
            # Update the async_tests instance variable
            self.async_tests.extend(async_tests)

    def load_test_files(self, path):
        """
        Auto-detect python files from a test suite folder/file path to a list
        Files can be under any nested folder
        """
        if path.endswith("__pycache__"):
            return
        if os.path.isfile(path) and path.endswith('.py'):
            self.test_files.append(path)
        elif os.path.isdir(path):
            for nested_path in os.listdir(path):
                self.load_test_files(path + "/" + nested_path)

    def setup_testsuite(self):
        """
        Run before test suite execution
        - Load the python files from the input path provided
        - Load all the @test decorated functions from the list of python files
        """
        # Logging
        test_rest_api_logger.info(str_color.info('Starting test setup'))
        test_rest_api_logger.info(str_color.info('Auto detecting test suites'))
        # Load python files
        self.load_test_files(self.test_suite_path)
        # Logging
        test_rest_api_logger.info(str_color.info(f'Total test suites: {len(self.test_files)}'))
        test_rest_api_logger.info(str_color.info('Auto detecting tests'))
        # Load @test decorated functions from the loaded python files
        self.load_tests()
        # Logging
        test_rest_api_logger.info(str_color.info(f'Total synchronous tests: {len(self.sync_tests)}'))
        test_rest_api_logger.info(str_color.info(f'Total asynchronous tests: {len(self.async_tests)}'))
        test_rest_api_logger.info(str_color.info(f'Total tests: {len(self.sync_tests) + len(self.async_tests)}'))

    @staticmethod
    def console_branding():
        """
        Package branding in Console
        """
        test_rest_api_logger.info(str_color.brand(f'''
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        '''))

    @staticmethod
    def console_summary():
        """
        Test Summary in Console
        """
        test_rest_api_logger.info(str_color.brand('''
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          ======================================================='''))
        test_rest_api_logger.info(str_color.info(f'''
                         {'Status:' : <20}{'PASS' if report.summary.test.status else 'FAIL'}
                         {'Tests:' : <20}{report.summary.tests.total}
                         {'Start:' : <20}{report.summary.test.start}
                         {'End:' : <20}{report.summary.test.end}
                         {'Duration:' : <20}{report.summary.test.duration}
                         {'Tags:' : <20}{report.summary.test.tags}
                         
                         {'PASS:' : <20}{report.summary.tests.success}
                         {'FAIL:' : <20}{report.summary.tests.fail}
                         {'ERROR:' : <20}{report.summary.tests.error}
                         {'DISABLE:' : <20}{report.summary.tests.disable}
                         {'SKIP:' : <20}{report.summary.tests.skip}
                         
                         {'LOW:' : <20}{report.summary.bugs.low}
                         {'MINOR:' : <20}{report.summary.bugs.minor}
                         {'MAJOR:' : <20}{report.summary.bugs.major}
                         {'CRITICAL:' : <20}{report.summary.bugs.critical}
                         {'BLOCKER:' : <20}{report.summary.bugs.blocker}
                         
                         {'REST API:' : <20}{report.summary.errors.rest_api}
                         {'GLOBAL VARIABLES:' : <20}{report.summary.errors.global_variables}
                         {'BUG:' : <20}{report.summary.errors.bug}
                         {'ASSERTION:' : <20}{report.summary.errors.assertion}
                         {'UNEXPECTED:' : <20}{report.summary.errors.unexpected}'''))

    def create_test_report(self):
        """
        Create and save the test report
        """
        # Create the report
        report.save(path=self.test_result_path)

    async def run_testsuite(self):
        """
        Run the test suite
        """
        # Package Branding in console
        Runner.console_branding()
        # Set up the testsuite before run
        self.setup_testsuite()
        # Exit if the total testcases = 0
        if len(self.sync_tests) + len(self.async_tests) == 0:
            sys.exit(ErrorMsg.EMPTY_TESTS)
        # Sort the synchronous tests
        self.sync_tests.sort(key=lambda x: x.execution_order)
        # Session should be created inside async function even if it itself not an async function
        # Also creation should happen inside the main event loop (Should not be in a separate event loop)
        session = aiohttp.ClientSession(json_serialize=json.dumps)
        # Create an aiohttp session for the whole run instead of creating a new session per request.
        AioHttpSession.set(session=session)
        # Logging
        test_rest_api_logger.info(str_color.info('Created aiohttp client session'))
        test_rest_api_logger.info(str_color.info('Completed test setup'))
        if len(self.sync_tests) > 0:
            test_rest_api_logger.info(str_color.brand("""
                          =======================================================
                        || ................  S Y N C - T E S T S ............... ||
                          ======================================================="""))
        # Start the stopwatch / counter
        timer_start = perf_counter_ns()
        # Test start date time
        start = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # Run synchronous tests before async tests
        for sync_test in (sync_test for sync_test in self.sync_tests):
            await sync_test()
        # Logging
        if len(self.async_tests) > 0:
            test_rest_api_logger.info(str_color.brand("""
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          ======================================================="""))
        # Running Tasks Concurrently (Execute async functions concurrently)
        # Run all async functions from tests list in parallel
        await asyncio.gather(*[async_test() for async_test in self.async_tests], return_exceptions=False)
        # Test end time
        end = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        # Stop the stopwatch / counter
        timer_stop = perf_counter_ns()
        # Calculate the time duration of the test in seconds (note: duration is in nanoseconds)
        duration = f'{(timer_stop - timer_start) / 1000000000} seconds'
        # Update report summary details
        report.summary.test.start = start
        report.summary.test.end = end
        report.summary.test.duration = duration
        report.summary.test.tags = self.test_tags
        # Close the aiohttp session after completing the test
        await AioHttpSession().close()
        # Create the test report
        self.create_test_report()
        # Summary Result in console
        Runner.console_summary()

    def run(self, test_suite_path: str, test_result_path: str, test_tags: list = []):
        """
        Method to run the testsuite
        This method can be used by the users to trigger the test in code.
        example:
                from test_rest_api import runner
                runner.run(test_suite_path="<Test Suite Path>", test_result_path="<Test Result Path>")

        This is also used by package in __main__.py to enable command line test execution
        example:
                python -m test_rest_api -t "<Test Suite Path>" -r "<Test Result Path> -h #smoke#sanity
        """
        try:
            # Validate if the path provided for test suite file/folder is valid
            if not os.path.exists(test_suite_path):
                sys.exit(ErrorMsg.INVALID_TEST_SUITE_PATH)
            # Update the path in test_suite_path instance variable
            self.test_suite_path = test_suite_path
            # Validate if the path provided for test result folder is valid
            if not os.path.isdir(test_result_path):
                sys.exit(ErrorMsg.INVALID_TEST_RESULT_PATH)
            # Update the path in test_result_path instance variable
            self.test_result_path = test_result_path
            # Validate tags
            if not isinstance(test_tags, list):
                sys.exit(ErrorMsg.INVALID_TEST_TAG)
            # Update the test tags in test_tags instance variable
            self.test_tags = test_tags
            # Run 'run_testsuite' coroutine in an event loop.
            asyncio.run(self.run_testsuite())
        except Exception as exc:
            sys.exit(f"""
{ErrorMsg.UNKNOWN_EXCEPTION}
Error details: {exc}
{traceback.format_exc()}
""")


runner = Runner()
