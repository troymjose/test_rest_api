import os
import sys
import json
import traceback
import types
import aiohttp
import asyncio
import importlib.machinery
from datetime import datetime
from inspect import getmembers, iscoroutinefunction
from test_rest_api.utils.colors import colors
from test_rest_api.reporting.report import report
from test_rest_api.utils.error_msg import ErrorMsg
from test_rest_api.utils.logger import test_rest_api_logger
from test_rest_api.utils.aiohttp_session import AioHttpSession


class Runner:
    """
    Execute all test cases
    Auto detect test suites and test cases
    """

    def __init__(self):
        # Test suite path
        self.path: str = ''
        # List of file paths
        self.test_files: list = []
        # List of @test decorated function objects
        self.tests: list = []

    def load_module(self, file: str):
        """
        Load the module in runtime and return it
        """
        # Create module path from file path
        name = file.replace(self.path, '').replace('/', '.')[1:-3]
        # Load the module
        loader = importlib.machinery.SourceFileLoader(name, file)
        module = types.ModuleType(name)
        loader.exec_module(module)
        # Return the module
        return module

    def load_test_file_tests(self, mod):
        """
        From test file load all the @test decorated function objects in a list
        Conditions: Is Async Function & Decorated with @test
        """
        return [obj for _, obj in getmembers(mod) if
                iscoroutinefunction(obj) and obj.__dict__.get('is_testcase', False)]

    def load_tests(self):
        """
        Auto-detect @test decorated functions from the list of test python files
        Update the function objects in tests list
        """
        # For each file path in list of python files from testsuite folder
        for test_file in self.test_files:
            # Load the module in runtime from file paths
            module = self.load_module(test_file)
            # Load the @test decorated functions as a list from the module
            tests = self.load_test_file_tests(module)
            # Update the tests instance variable
            self.tests.extend(tests)

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
        test_rest_api_logger.info(f"{colors.LIGHT_PURPLE}Starting test setup{colors.LIGHT_CYAN}")
        test_rest_api_logger.info(f"{colors.LIGHT_PURPLE}Test Suite: {self.path}{colors.LIGHT_CYAN}")
        test_rest_api_logger.info(f'{colors.LIGHT_PURPLE}Auto detecting test suites{colors.LIGHT_CYAN}')
        # Load python files
        self.load_test_files(self.path)
        # Logging
        test_rest_api_logger.info(
            f'{colors.LIGHT_PURPLE}{len(self.test_files)} test suites detected{colors.LIGHT_CYAN}')
        test_rest_api_logger.info(f'{colors.LIGHT_PURPLE}Auto detecting tests{colors.LIGHT_CYAN}')
        # Load @test decorated functions from the loaded python files
        self.load_tests()
        # Logging
        test_rest_api_logger.info(f'{colors.LIGHT_PURPLE}{len(self.tests)} tests detected{colors.LIGHT_CYAN}')

    @staticmethod
    def console_branding():
        """
        Package branding in Console
        """
        test_rest_api_logger.info(f'''{colors.LIGHT_PURPLE}
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        {colors.LIGHT_CYAN}''')

    @staticmethod
    def console_summary():
        """
        Test Summary in Console
        """
        test_rest_api_logger.info(f'''{colors.LIGHT_PURPLE}
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        {colors.LIGHT_CYAN}Test Status: {colors.LIGHT_PURPLE}{'PASS' if report.summary.status else 'FAIL'}
                        {colors.LIGHT_CYAN}Total tests: {colors.LIGHT_PURPLE}{report.summary.total}
                        {colors.LIGHT_CYAN}Test Duration: {colors.LIGHT_PURPLE}{report.summary.duration}''')

    async def run_testsuite(self):
        """
        Run the test suite
        """
        # Package Branding in console
        Runner.console_branding()
        # Set up the testsuite before run
        self.setup_testsuite()
        # Logging
        test_rest_api_logger.info(f"{colors.LIGHT_PURPLE}Completed test setup{colors.LIGHT_CYAN}")
        test_rest_api_logger.info(f"{colors.LIGHT_PURPLE}Creating aiohttp client session{colors.LIGHT_CYAN}")
        # Session should be created inside async function even if it itself not an async function
        # Also creation should happen inside the main event loop (Should not be in a separate event loop)
        session = aiohttp.ClientSession(json_serialize=json.dumps)
        # Create an aiohttp session for the whole run instead of creating a new session per request.
        AioHttpSession.set(session=session)
        # Logging
        test_rest_api_logger.info(f"{colors.LIGHT_PURPLE}Created aiohttp client session{colors.LIGHT_CYAN}")
        test_rest_api_logger.info(f"{colors.LIGHT_PURPLE}Starting async test execution{colors.LIGHT_CYAN}")
        # Test start time
        start = datetime.now()
        # Running Tasks Concurrently (Execute async functions concurrently)
        # Run all async functions from tests list in parallel
        await asyncio.gather(*[test() for test in self.tests], return_exceptions=False)
        # Test end time
        end = datetime.now()
        # Logging
        test_rest_api_logger.info(f"{colors.LIGHT_PURPLE}Completed async test execution{colors.LIGHT_CYAN}")
        # Update report summary details
        report.summary.duration = end - start
        report.summary.start = start.strftime('%Y-%m-%d %H:%M:%S')
        report.summary.end = end.strftime('%Y-%m-%d %H:%M:%S')
        report.summary.status = 'PASS' if report.summary.status else 'FAIL'
        # Close the aiohttp session after completing the test
        await AioHttpSession().close()
        # Summary Result in console
        Runner.console_summary()

    def run(self, path: str):
        """
        Method to run the testsuite
        This method can be used by the users to trigger the test in code.
        example:
                from test_rest_api import runner
                runner.run(path="<Test Suite Path>")
        This is also used by package in __main__.py to enable command line test execution
        example:
                python -m test_rest_api run "<Test Suite Path>"
        """
        try:
            # Validate if the path provided for test suite file/folder is valid
            if not os.path.exists(path):
                sys.exit(ErrorMsg.INVALID_PATH)
            # Update the path in instance variable
            self.path = path
            # Run 'run_testsuite' coroutine in an event loop.
            asyncio.run(self.run_testsuite())
        except Exception as exc:
            sys.exit(f"""
{ErrorMsg.UNKNOWN_EXCEPTION}
Error details: {exc}
{traceback.format_exc()}
""")


runner = Runner()