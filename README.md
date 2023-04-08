<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/assets/test_rest_api.png"  width="50%" >

# TEST REST API

Create fast modern __asynchronous__ tests for __REST API__ testing

```#FAST #EASY #ASYNC #RESTAPI #TESTING #AUTOMATION```

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
    - [Basic usage](#1-basic-usage)
    - [Set report path](#2-set-report-path)
    - [Set .env path](#3-set-env-path)
    - [Set hashtags](#4-set-hashtags)
    - [Project structure](#5-project-structure)
- [Examples](#examples)
    - [My first test](#1-my-first-test)
    - [Configure my test](#2-configure-my-test)
    - [My first logger](#3-my-first-logger)
    - [Set global variables value](#4-set-global-variables-value)
    - [Set global variables value as constant](#5-set-global-variables-value-as-constant)
    - [Get global variables value](#6-get-global-variables-value)
    - [My first bug](#7-my-first-bug)
    - [Configure my bug](#8-configure-my-bug)
    - [My first rest api](#9-my-first-rest-api)
    - [Configure my rest api](#10-configure-my-rest-api)
    - [Reuse my rest api](#11-reuse-my-rest-api)
    - [Send my rest api](#12-send-my-rest-api)
    - [Rest api response](#13-rest-api-response)
    - [Demo with all the above features](#14-demo)
- [Reports](#reports)
    - [My first report](#1-my-first-report)
    - [Async tests report](#2-async-tests-report)
    - [Sync tests report](#3-sync-tests-report)
    - [Sync & Async report](#4-sync-and-async-report)
    - [Multi status report](#5-multi-status-report)
    - [Multi bug report](#6-multi-bug-report)
    - [Rest api errors](#7-rest-api-errors)
    - [Global variables errors](#8-global-variables-errors)
    - [Bug errors](#9-bug-errors)
    - [Logger errors](#10-logger-errors)
    - [Unexpected errors](#11-unexpected-errors)
- [Author](#author)
- [License](#license)

<h2 id="features">Features</h2>

- __Asyncronus__ programming (Powered by [asyncio](https://pypi.org/project/asyncio/))
- __Auto discovery__ of test modules and functions
- Supports both __asyncronus__ & __syncronuous__ tests
- __High speed__ test executions using async functions
- __Html test reporting__ with custom logs & summary dashboards
- Create complex flows using __parameterization__ & __correlation__
- __Group__ similar tests using hashtags eg: __#smoke__
- Supports __CI/CD__ test automation integrations
- Designed to be __easy__ to use & learn

<h2 id="installation">Installation</h2>

If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:

```pip install test_rest_api```

<h2 id="usage">Usage</h2>

<h4 id="1-basic-usage">1. Basic usage</h4>

- - -

__Syntax__

``` python -m test_rest_api -t "<Test folder/file path>" ```

- Tests are executed from the __command line__ using the test_rest_api module directly
- The basic usage is by giving a __file path__ or __directory path__ as an argument
- __-t__ stands for Test suite path
- We can __organise__ folders, sub folders and python files in any __custom__ structure
- test_rest_api will __autodetect__ python files and folders as __Test suites__

<h4 id="2-set-report-path">2. Set report path</h4>

- - -

__Syntax__

``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" ```

- In the above example, __html test report__ is saved under the same test folder path
- We can save the final report to our __custom path__ by providing __-r__ followed by path
- __-r__ stands for Report path
- test_rest_api __creates__ beautiful rich test report with summary dashboards
- We can also add our __custom logs__ to each individual tests in the test report

<h4 id="3-set-env-path">3. Set .env path</h4>

- - -

__Syntax__

```
python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path"
```

- We can __set variables__ with values, example Domain, Username, Password etc. in __.env file__
- test_rest_api will __auto fetch__ all these values and save under __Global Variables__ as constants
- Global Variables can be accessed in tests for __parametrization__
- One example can be __dynamic__ url creation. Domain can be __parameterised__ in url creation
- This will also help developers to run the same tests in __different environments__ by creating separate .env files
- We can __set__ the environment variables by providing __-e__ followed by path
- __-e__ stands for Environment path

<h4 id="4-set-hashtags">4. Set hashtags</h4>

- - -

__Syntax__

```
python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" -e ".env file path" -h #SMOKE#SANITY
```

- __Group__ your test by providing tags in test creation
- This helps to __execute__ a group of testcases, example __smoke testing__, __regression testing__ etc.
- test_rest_api will fetch all tests with the __provided tags__ in the command line and executes them
- We can set the __hashtags__ for execution by providing __-h__ followed by tags, example __#SMOKE#SANITY__
- __-h__ stands for Hashtags
- When __no__ tags are provided, __all the tests__ are executed
- When we provide a __single tag__, only those testcases with that tag are executed
- Some tests like login should __run always__ for all tags irrespective of the value
- In this case it's not practical to add all tags to the login test function
- Adding __all tags__ will be hard to maintain when we introduce new custom tags
- To tackle this issue, we can use inbuilt __#ALL tag__
- __#ALL__ tagged tests will always be executed. It will not be skipped
- Tests like login, logout etc. are __perfect candidates__ for #ALL

<h4 id="5-project-structure">5. Project structure</h4>

- - -

```
.
├── api                           # Store all your rest api files
│   ├── auth                      # Custom structure for subfolders & files
│   │   ├── login.py              # Python file to store rest_api code
│   │   │   ├── def user_login()  # Python function to create rest_api
│   │   │   ├── def admin_login()
│   │   │   └── ...    
│   │   └── ...
│   └── ...
├── testsuite                     # Root testsuite folder
│   ├── auth                      # Custom structure for subfolders & files
│   │   ├── login.py              # Python file as testsuite to store tests
│   │   │   ├── async def t001()  # Python async function as testcases
│   │   │   ├── async def t002()
│   │   │   └── ...    
│   │   └── ...
│   └── ...
└── ...
```

- 2 sub folders __api__ & __testsuite__
- Any __custom names__ can be used instead of __api__ & __testsuite__
- __api__ should store all the api creation python files
- __testsuite__ should store all the test creation python files
- Any __custom structure__ with multiple sub folders can be used to organise the files
- __Separating__ api from tests will avoid __code duplication__ for rest_api creation
- Root testsuite folder __path__ will be used in command line __execution__ value for __-t__

<h2 id="examples">Examples</h2>

<h4 id="1-my-first-test">1. My first test</h4>

- - -

```python
from test_rest_api import test


@test()
async def my_first_test():
    return None
```   

- Create an __async__ python function with any __custom__ name
- Decorate the function using __@test()__
- __Async__ python functions decoratd with __@test()__ will be auto-detected as testcase
- __Normal__ python functions decoratd with __@test()__ will __not__ be considered as testcase

__Congrats !__

You have successfully created your first test (__my_first_test__)

Now let's __execute__ it from command line . . .

- __Create__ a
  python [virtual environment](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
- Install __test_rest_api__ using __command__ ```pip install test_rest_api```
- Create new python file (eg: __my_first_testsuite.py__) and paste the above code
- Execute the test from the __command line__ using the test_rest_api module directly

``` python -m test_rest_api -t "<Test folder/file path>" -r "Result folder path" ```

<h4 id="2-configure-my-test">2. Configure my test</h4>

- - -

```python
from test_rest_api import test


@test(name='Custom Name', desc='Description', enabled=True, tags=['SMOKE', 'ABC'], is_async=True, execution_order='1')
async def my_second_test():
    return None
```

- In our first example, we used @test() decorator with __empty parameters__
- In this example, we are __using parameters__ to configure our test function
- This can be considered as adding __settings__ to your test function


- __name__
    - Mandatory: False
    - Data Type: str
    - Expected: Custom name for your test
    - Default: Function name
- __desc__
    - Mandatory: False
    - Data Type: str
    - Expected: Test description
    - Default: Empty string
- __enabled__
    - Mandatory: False
    - Data Type: bool
    - Expected: True or False. Provide False, to disable the test
    - Default: True
- __tags__
    - Mandatory: False
    - Data Type: list
    - Expected: List of tags. Group your tests with custom tags
    - Default: Empty list
- __is_async__
    - Mandatory: False
    - Data Type: bool
    - Expected: True or False. Provide False, to run tests sequentially
    - Default: True
- __execution_order__
    - Mandatory: False
    - Data Type: str
    - Expected: Custom text for ordering. This will work only when is_async = False
    - Default: 'zzzzz'

<h4 id="3-my-first-logger">3. My first logger</h4>

- - -

```python
from test_rest_api import test, Logger


@test()
async def my_first_logger():
    logger = Logger()
    logger.log("my 1st log")
    logger.log("my 2nd log")
    return logger 
```

- Loggers are used to add __custom messages__ to the final html test report
- Create a new Logger __instance__ inside your test function```logger = Logger()```
- Logger instance __name__ can be any custom text. Here we have used __logger__
- Add any number of log messages using __log method__ ```logger.log("my 1st log")```
- Return logger instance for rich test __reporting__ ```return logger```
- It is __recommended__ to use logger for all your tests

<h4 id="4-set-global-variables-value">4. Set global variables value</h4>

- - -

```python
from test_rest_api import test, GlobalVariables


@test()
async def set_global_variables_value():
    GlobalVariables.set(name='token', value='token from response')
```

- Global variables are used to __save__ & __retrieve__ values in runtime
- This will help in __parameterization__ and __correlation__ of tests
- Save __Token__ from login api response in your first test
- Retrieve this Token in all your __upcoming tests__ for authentication
- Here we will learn how to __set__ the value in GlobalVariables

```GlobalVariables.set(name='token', value='token from response')```

- __name__
    - Mandatory: True
    - Data Type: str
    - Expected: Custom name for your global variable
- __value__
    - Mandatory: True
    - Data Type: any
    - Expected: Any python data type can be stored as global variables value

<h4 id="5-set-global-variables-value-as-constant">5. Set global variables value as constant</h4>

- - -

```python
from test_rest_api import test, GlobalVariables


@test()
async def set_global_variables_value_as_constant():
    GlobalVariables.set(name='pi', value=3.14, is_constant=True)
```

- In the above example we learned to __set__ value to global variables
- __Multiple set__ calls are possible for the same variable
- Token variable can be __set again__ in a different test function
- To avoid this, we can set global variables as a __constant__ value
- Use __is_consant__ optional parameter & make it True

```GlobalVariables.set(name='pi', value=3.14, is_constant=True)```

- __name__
    - Mandatory: True
    - Data Type: str
    - Expected: Custom name for your global variable
- __value__
    - Mandatory: True
    - Data Type: any
    - Expected: Any python data type can be stored as global variables value
- __is_constant__
    - Mandatory: False
    - Data Type: bool
    - Expected: True or False. Provide True, to create constants
    - Default: False

<h4 id="6-get-global-variables-value">6. Get global variables value</h4>

- - -

```python
from test_rest_api import test, GlobalVariables


@test()
async def get_global_variables_value():
    token: str = GlobalVariables.get(name='token')
    pi: float = GlobalVariables.get(name='pi')
```

- In the above examples we learned to __set__ varying and constant value to global variables
- Now it's time to __retrieve__ them in our tests
- Please make sure to use __valid variable names__ while retrieving the values
- If the variable name is __not present__ in global variables, test will __terminate with error__

```GlobalVariables.get(name='token')```

- __name__
    - Mandatory: True
    - Data Type: str
    - Expected: Valid name of any saved global variable

<h4 id="7-my-first-bug">7. My first bug</h4>

- - -

```python
from test_rest_api import test, Bug


@test()
async def my_first_bug():
    Bug()
```

- Bug is used to __raise issues__ in tests
- Add custom __checks__ in your tests to validate __rest api response__
- If __actual result__ is not the __expected result__, just call ```Bug()```
- This will __terminate__ the current test function execution
- Bug __details__ can be viewed in final html test __report__

<h4 id="8-configure-my-bug">8. Configure my bug</h4>

- - -

```python
from test_rest_api import test, Bug, Logger


@test()
async def my_second_bug():
    logger = Logger()
    logger.log('step 1')
    logger.log('step 2')
    logger.log('Consider all steps are logged')
    Bug(message="msg", priority=Bug.PRIORITY.BLOCKER, actual_result="", expected_result="", steps_to_reproduce=logger)
```

- In our first bug example, we used Bug() with __empty attributes__
- In this example, we are __using attributes__ to configure our Bug
- This can be considered as adding __more info__ to your bug in the final html test report
- We are adding custom __logging__ in this example to show how logger instance is __useful in Bug creation__
- Logger instance variable can be passed to __steps_to_reproduce__ attribute during Bug creation

```
Bug(message='', priority='', actual_result='', expected_result='', steps_to_reproduce='')
```

- __message__
    - Mandatory: False
    - Data Type: str
    - Expected: Custom message for your bug
    - Default: Empty string
- __priority__
    - Mandatory: False
    - Data Type: str
    - Expected: Priority for this bug. Supported list: Bug.PRIORITY.__[ items ]__
    - Default: Empty string
- __actual_result__
    - Mandatory: False
    - Data Type: str
    - Expected: Provide the actual result
    - Default: Empty string
- __expected_result__
    - Mandatory: False
    - Data Type: str
    - Expected: Provide the expected result
    - Default: Empty list
- __steps_to_reproduce__
    - Mandatory: False
    - Data Type: str
    - Expected: Logger instance can be used to auto-populate this field
    - Default: Empty string

<h4 id="9-my-first-rest-api">9. My first rest api</h4>

- - -

```python
from test_rest_api import test, RestApi


@test()
async def my_first_rest_api():
    rest_api = RestApi(url='https://dummyjson.com/products/1')
```

- RestApi is used __create__ rest api instance in tests
- Here we have created a basic rest api with just the __url information__
- This example is only about creating rest api, no __send action__ is performed here
- We will use this __instance variable__ for sending the request in upcoming examples

<h4 id="10-configure-my-rest-api">10. Configure my rest api</h4>

- - -

```python
from test_rest_api import test, RestApi


@test()
async def configure_my_rest_api():
    rest_api = RestApi(url='my url', parameters={'p1': 'v1', 'p2': 'val2'}, headers={'h1': 'v1', 'h2': 'val1'}, body={})
```

- In the above example, we have only used __url attribute__ for rest api creation
- Other attributes for creation are __parameters__, __headers__ and __body__
- This example shows the syntax for adding these __optional attributes__


- __url__
    - Mandatory: True
    - Data Type: str
    - Expected: Rest api url
- __parameters__
    - Mandatory: False
    - Data Type: dict
    - Expected: Key value pairs of parameter name & value
    - Default: {}
- __headers__
    - Mandatory: False
    - Data Type: dict
    - Expected: Key value pairs of header name & value
    - Default: {}
- __body__
    - Mandatory: False
    - Data Type: dict
    - Expected: Provide the json request payload
    - Default: {}

<h4 id="11-reuse-my-rest-api">11. Reuse my rest api</h4>

- - -

```python
from test_rest_api import RestApi, GlobalVariables


def login_api(username: str, password: str):
    domain = GlobalVariables.get('DOMAIN')
    url = f'https://{domain}/login'
    body = {'username': username, 'password': password}
    return RestApi(url=url, body=body)
```

- A rest api will be used for __multiple tests__
- __Creation__ of rest api __inside__ test async functions will result in __code duplication__
- Duplicate code makes your program __lengthy__ and decreases your code __quality__
- __Updating__ & __maintaining__ this rest api creations in __multiple__ tests will be difficult
- __New changes__ to rest api, will result in changing the __same code multiple times__
- To avoid duplication, we can use a __separate folder__ for rest api files
- Use python __functions__ to create a rest api which will avoid __code duplication__
- You can __call__ a function __100__ times instead of __writing__ it __100__ times
- In this example we have created a simple __login api__
- All the __dynamic values__ for rest api creation can be passed as function __parameters__
- This helps in calling the same api with __different inputs__
- Return the __RestApi instance__ which can be used in test functions for __sending__

<h4 id="12-send-my-rest-api">12. Send my rest api</h4>

- - -

```python
from test_rest_api import test, RestApi


@test()
async def send_my_rest_api():
    rest_api = RestApi(url='https://dummyjson.com/products/1')
    response1 = await rest_api.get()
    response2 = await rest_api.send(method='get')
    response3 = await rest_api.send(method=rest_api.METHODS.GET)
```

- In the above examples, we learned to __create__ a rest api
- Now it's time to __send__ them using http methods
- __Supported__ http methods are GET, POST, PUT, PATCH, DELETE, OPTIONS & HEAD
- Here we are sending the rest_api using __GET__ http method
- All the responses (1, 2 & 3) will have the __same result__
- Because they perform the same functionality with __different syntax__
- Similarly, __other http methods__ can be used, with your desired syntax

<h4 id="13-rest-api-response">13. Rest api response</h4>

- - -

```python
from test_rest_api import test, RestApi


@test()
async def send_my_rest_api():
    rest_api = RestApi(url='https://dummyjson.com/products/1')
    response = await rest_api.get()

    status_code = response.status_code
    body = response.body
    headers = response.headers
    content_type = response.content_type
    obj = response.obj
```

- We have covered rest api __creation__ & __sending__ part
- Now lets see more about the __response object__
- Mostly __all checks__ will be performed using response object data
- Response object contains the below details


- __response.status_code__
    - Data Type: int
    - Value: Response status code
- __response.body__
    - Data Type: dict
    - Value: Response body
- __response.headers__
    - Data Type: dict
    - Value: Response headers
- __response.content_type__
    - Data Type: str
    - Value: Response content type
- __response.obj__
    - Data Type: aiohttp.ClientResponse
    - Value: Python aiohttp ClientResponse object

<h4 id="14-demo">14. Demo with all the above features</h4>

- - -

```
.env file
---------

DOMAIN=dummyjson.com
```

```python
from test_rest_api import test, RestApi, Bug, Logger, GlobalVariables


@test(name='Demo', desc='All features')
async def demo():
    logger = Logger()
    logger.log('Starting the test')

    logger.log('Creating rest api')
    domain = GlobalVariables.get('DOMAIN')
    rest_api = RestApi(url=f"https://{domain}/products/1")

    logger.log('Sending rest api')
    response = await rest_api.get()

    logger.log(f'Response code = {response.status_code}')
    logger.log(f'Response body = {response.body}')

    logger.log('Validate response code')
    if response.status_code != 200:
        Bug(message='Invalid status code', priority=Bug.PRIORITY.MINOR, actual_result=response.status_code,
            expected_result='200', steps_to_reproduce=logger)

    logger.log('Save price details to global variables')
    title = response.body.get('title', '')
    price = response.body.get('price', '')
    GlobalVariables.set(name=title, value=price)

    logger.log('Successfully completed the test')

```

<h2 id="reports">Reports</h2>

<h4 id="1-my-first-report">1. My first report</h4>

- - -

- Single basic test with __PASS__ status

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/my_first_report.html)

Console output

```bash
2023-04-08 15:40:22,712: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 15:40:22,712: Starting test setup
2023-04-08 15:40:22,712: Auto detecting test suites
2023-04-08 15:40:22,712: Total test suites: 1
2023-04-08 15:40:22,712: Auto detecting tests
2023-04-08 15:40:22,713: Total synchronous tests: 0
2023-04-08 15:40:22,714: Total asynchronous tests: 1
2023-04-08 15:40:22,714: Total tests: 1
2023-04-08 15:40:22,714: Created aiohttp client session
2023-04-08 15:40:22,714: Completed test setup
2023-04-08 15:40:22,714: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 15:40:22,714: PASS    my_first_test (root file) [1]
2023-04-08 15:40:22,715: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             PASS
                        Tests:              1
                        Start:              2023-04-08 15-40-22
                        End:                2023-04-08 15-40-22
                        Duration:           0.000956233 seconds
                        Tags:               []
                        
                        PASS:               1
                        FAIL:               0
                        ERROR:              0
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="2-async-tests-report">2. Async tests report</h4>

- - -

- 5 __async__ tests
- Each tests takes __1 second__ to complete

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/async_tests_report.html)

Console output

```bash
2023-04-08 15:52:05,062: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 15:52:05,062: Starting test setup
2023-04-08 15:52:05,062: Auto detecting test suites
2023-04-08 15:52:05,062: Total test suites: 1
2023-04-08 15:52:05,062: Auto detecting tests
2023-04-08 15:52:05,063: Total synchronous tests: 0
2023-04-08 15:52:05,063: Total asynchronous tests: 5
2023-04-08 15:52:05,063: Total tests: 5
2023-04-08 15:52:05,063: Created aiohttp client session
2023-04-08 15:52:05,063: Completed test setup
2023-04-08 15:52:05,063: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 15:52:06,064: PASS    testcase_1 (root file) [1]
2023-04-08 15:52:06,064: PASS    testcase_2 (root file) [2]
2023-04-08 15:52:06,065: PASS    testcase_3 (root file) [3]
2023-04-08 15:52:06,065: PASS    testcase_4 (root file) [4]
2023-04-08 15:52:06,065: PASS    testcase_5 (root file) [5]
2023-04-08 15:52:06,066: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             PASS
                        Tests:              5
                        Start:              2023-04-08 15-52-05
                        End:                2023-04-08 15-52-06
                        Duration:           1.002069748 seconds
                        Tags:               []
                        
                        PASS:               5
                        FAIL:               0
                        ERROR:              0
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="3-sync-tests-report">3. Sync tests report</h4>

- - -

- 5 __sync__ tests
- Each tests takes __1 second__ to complete

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/sync_tests_report.html)

Console output

```bash
2023-04-08 15:56:19,128: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 15:56:19,129: Starting test setup
2023-04-08 15:56:19,129: Auto detecting test suites
2023-04-08 15:56:19,129: Total test suites: 1
2023-04-08 15:56:19,129: Auto detecting tests
2023-04-08 15:56:19,129: Total synchronous tests: 5
2023-04-08 15:56:19,129: Total asynchronous tests: 0
2023-04-08 15:56:19,129: Total tests: 5
2023-04-08 15:56:19,129: Created aiohttp client session
2023-04-08 15:56:19,129: Completed test setup
2023-04-08 15:56:19,130: 
                          =======================================================
                        || ................  S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 15:56:20,131: PASS    testcase_1 (root file) [1]
2023-04-08 15:56:21,132: PASS    testcase_2 (root file) [2]
2023-04-08 15:56:22,132: PASS    testcase_3 (root file) [3]
2023-04-08 15:56:23,134: PASS    testcase_4 (root file) [4]
2023-04-08 15:56:24,135: PASS    testcase_5 (root file) [5]
2023-04-08 15:56:24,137: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             PASS
                        Tests:              5
                        Start:              2023-04-08 15-56-19
                        End:                2023-04-08 15-56-24
                        Duration:           5.006235552 seconds
                        Tags:               []
                        
                        PASS:               5
                        FAIL:               0
                        ERROR:              0
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="4-sync-and-async-report">4. Sync & Async report</h4>

- - -

- 5 __sync__ & __async__ tests each
- Total __10__ tests
- Each tests takes __1 second__ to complete

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/sync_and_async_report.html)

Console output

```bash
2023-04-08 15:59:38,170: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 15:59:38,170: Starting test setup
2023-04-08 15:59:38,170: Auto detecting test suites
2023-04-08 15:59:38,170: Total test suites: 1
2023-04-08 15:59:38,170: Auto detecting tests
2023-04-08 15:59:38,172: Total synchronous tests: 5
2023-04-08 15:59:38,172: Total asynchronous tests: 5
2023-04-08 15:59:38,172: Total tests: 10
2023-04-08 15:59:38,173: Created aiohttp client session
2023-04-08 15:59:38,173: Completed test setup
2023-04-08 15:59:38,173: 
                          =======================================================
                        || ................  S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 15:59:39,174: PASS    testcase_1 (root file) [1]
2023-04-08 15:59:40,176: PASS    testcase_2 (root file) [2]
2023-04-08 15:59:41,177: PASS    testcase_3 (root file) [3]
2023-04-08 15:59:42,178: PASS    testcase_4 (root file) [4]
2023-04-08 15:59:43,180: PASS    testcase_5 (root file) [5]
2023-04-08 15:59:43,180: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 15:59:44,182: PASS    testcase_async_1 (root file) [6]
2023-04-08 15:59:44,182: PASS    testcase_async_2 (root file) [7]
2023-04-08 15:59:44,183: PASS    testcase_async_3 (root file) [8]
2023-04-08 15:59:44,183: PASS    testcase_async_4 (root file) [9]
2023-04-08 15:59:44,183: PASS    testcase_async_5 (root file) [10]
2023-04-08 15:59:44,185: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             PASS
                        Tests:              10
                        Start:              2023-04-08 15-59-38
                        End:                2023-04-08 15-59-44
                        Duration:           6.01064299 seconds
                        Tags:               []
                        
                        PASS:               10
                        FAIL:               0
                        ERROR:              0
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="5-multi-status-report">5. Multi status report</h4>

- - -

- 5 __async__ tests with different __status__ values
- __Status list__: PASS, FAIL, ERROR, DISABLE & SKIP

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/multi_status_report.html)

Console output

```bash
2023-04-08 16:17:44,328: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 16:17:44,329: Starting test setup
2023-04-08 16:17:44,329: Auto detecting test suites
2023-04-08 16:17:44,329: Total test suites: 1
2023-04-08 16:17:44,329: Auto detecting tests
2023-04-08 16:17:44,330: Total synchronous tests: 0
2023-04-08 16:17:44,330: Total asynchronous tests: 5
2023-04-08 16:17:44,330: Total tests: 5
2023-04-08 16:17:44,330: Created aiohttp client session
2023-04-08 16:17:44,330: Completed test setup
2023-04-08 16:17:44,330: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 16:17:44,330: ERROR   t_error (root file) [2]
2023-04-08 16:17:44,331: FAIL    t_fail (root file) [3]
2023-04-08 16:17:44,331: PASS    t_pass (root file) [4]
2023-04-08 16:17:44,332: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             FAIL
                        Tests:              5
                        Start:              2023-04-08 16-17-44
                        End:                2023-04-08 16-17-44
                        Duration:           0.001355524 seconds
                        Tags:               ['SMOKE']
                        
                        PASS:               1
                        FAIL:               1
                        ERROR:              1
                        DISABLE:            1
                        SKIP:               1
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              1
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         1
```

<h4 id="6-multi-bug-report">6. Multi bug report</h4>

- 5 __async__ tests with different __bug priority__ values
- __Priority list__: LOW, MINOR, MAJOR, CRITICAL, BLOCKER

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/multi_bug_report.html)

Console output

```bash
2023-04-08 16:30:21,400: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 16:30:21,400: Starting test setup
2023-04-08 16:30:21,400: Auto detecting test suites
2023-04-08 16:30:21,400: Total test suites: 1
2023-04-08 16:30:21,400: Auto detecting tests
2023-04-08 16:30:21,401: Total synchronous tests: 0
2023-04-08 16:30:21,401: Total asynchronous tests: 5
2023-04-08 16:30:21,401: Total tests: 5
2023-04-08 16:30:21,402: Created aiohttp client session
2023-04-08 16:30:21,402: Completed test setup
2023-04-08 16:30:21,402: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 16:30:21,402: FAIL    t_blocker (root file) [1]
2023-04-08 16:30:21,404: FAIL    t_critical (root file) [2]
2023-04-08 16:30:21,404: FAIL    t_low (root file) [3]
2023-04-08 16:30:21,404: FAIL    t_major (root file) [4]
2023-04-08 16:30:21,404: FAIL    t_minor (root file) [5]
2023-04-08 16:30:21,406: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             FAIL
                        Tests:              5
                        Start:              2023-04-08 16-30-21
                        End:                2023-04-08 16-30-21
                        Duration:           0.003122595 seconds
                        Tags:               []
                        
                        PASS:               0
                        FAIL:               5
                        ERROR:              0
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                1
                        MINOR:              1
                        MAJOR:              1
                        CRITICAL:           1
                        BLOCKER:            1
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="7-rest-api-errors">7. Rest api errors</h4>

- - -

- Developers can make __errors__ while coding
- __General__ error exception __messages__ will increase the time to __find__ and __fix__ these issues
- test_rest_api provides __short__ & __precise__ error's with exact __traceback__ info
- Here we are __purposefully__ making errors in __RestApi__ functions

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/rest_api_errors.html)

Console output

```bash
2023-04-08 19:41:19,099: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 19:41:19,099: Starting test setup
2023-04-08 19:41:19,099: Auto detecting test suites
2023-04-08 19:41:19,099: Total test suites: 1
2023-04-08 19:41:19,099: Auto detecting tests
2023-04-08 19:41:19,099: Total synchronous tests: 0
2023-04-08 19:41:19,099: Total asynchronous tests: 12
2023-04-08 19:41:19,099: Total tests: 12
2023-04-08 19:41:19,099: Created aiohttp client session
2023-04-08 19:41:19,099: Completed test setup
2023-04-08 19:41:19,099: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 19:41:19,100: ERROR   t1 (root file) [1]
2023-04-08 19:41:19,101: ERROR   t10 (root file) [2]
2023-04-08 19:41:19,110: ERROR   t2 (root file) [5]
2023-04-08 19:41:19,110: ERROR   t3 (root file) [6]
2023-04-08 19:41:19,110: ERROR   t4 (root file) [7]
2023-04-08 19:41:19,110: ERROR   t5 (root file) [8]
2023-04-08 19:41:19,110: ERROR   t6 (root file) [9]
2023-04-08 19:41:19,111: ERROR   t7 (root file) [10]
2023-04-08 19:41:19,111: ERROR   t8 (root file) [11]
2023-04-08 19:41:19,111: ERROR   t9 (root file) [12]
2023-04-08 19:41:19,115: ERROR   t11 (root file) [3]
2023-04-08 19:41:19,285: ERROR   t12 (root file) [4]
2023-04-08 19:41:19,288: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             FAIL
                        Tests:              12
                        Start:              2023-04-08 19-41-19
                        End:                2023-04-08 19-41-19
                        Duration:           0.18714125 seconds
                        Tags:               []
                        
                        PASS:               0
                        FAIL:               0
                        ERROR:              12
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           12
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="8-global-variables-errors">8. Global variables errors</h4>

- - -

- Developers can make __errors__ while coding
- __General__ error exception __messages__ will increase the time to __find__ and __fix__ these issues
- test_rest_api provides __short__ & __precise__ error's with exact __traceback__ info
- Here we are __purposefully__ making errors in __GlobalVariables__ functions

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/global_variables_errors.html)

Console output

```bash
2023-04-08 18:38:05,825: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 18:38:05,825: Starting test setup
2023-04-08 18:38:05,825: Auto detecting test suites
2023-04-08 18:38:05,826: Total test suites: 1
2023-04-08 18:38:05,826: Auto detecting tests
2023-04-08 18:38:05,827: Total synchronous tests: 0
2023-04-08 18:38:05,827: Total asynchronous tests: 13
2023-04-08 18:38:05,827: Total tests: 13
2023-04-08 18:38:05,827: Created aiohttp client session
2023-04-08 18:38:05,827: Completed test setup
2023-04-08 18:38:05,827: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 18:38:05,827: ERROR   t_1 (root file) [1]
2023-04-08 18:38:05,828: ERROR   t_10 (root file) [2]
2023-04-08 18:38:05,828: ERROR   t_11 (root file) [3]
2023-04-08 18:38:05,828: ERROR   t_12 (root file) [4]
2023-04-08 18:38:05,829: ERROR   t_13 (root file) [5]
2023-04-08 18:38:05,829: ERROR   t_2 (root file) [6]
2023-04-08 18:38:05,829: ERROR   t_3 (root file) [7]
2023-04-08 18:38:05,829: ERROR   t_4 (root file) [8]
2023-04-08 18:38:05,829: ERROR   t_5 (root file) [9]
2023-04-08 18:38:05,830: ERROR   t_6 (root file) [10]
2023-04-08 18:38:05,830: ERROR   t_7 (root file) [11]
2023-04-08 18:38:05,830: ERROR   t_8 (root file) [12]
2023-04-08 18:38:05,830: ERROR   t_9 (root file) [13]
2023-04-08 18:38:05,831: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             FAIL
                        Tests:              13
                        Start:              2023-04-08 18-38-05
                        End:                2023-04-08 18-38-05
                        Duration:           0.003679225 seconds
                        Tags:               []
                        
                        PASS:               0
                        FAIL:               0
                        ERROR:              13
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   13
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="9-bug-errors">9. Bug errors</h4>

- - -

- Developers can make __errors__ while coding
- __General__ error exception __messages__ will increase the time to __find__ and __fix__ these issues
- test_rest_api provides __short__ & __precise__ error's with exact __traceback__ info
- Here we are __purposefully__ making errors in __Bug__ functions

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/bug_errors.html)

Console output

```bash
2023-04-08 19:55:51,870: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 19:55:51,871: Starting test setup
2023-04-08 19:55:51,871: Auto detecting test suites
2023-04-08 19:55:51,871: Total test suites: 1
2023-04-08 19:55:51,871: Auto detecting tests
2023-04-08 19:55:51,872: Total synchronous tests: 0
2023-04-08 19:55:51,872: Total asynchronous tests: 7
2023-04-08 19:55:51,872: Total tests: 7
2023-04-08 19:55:51,872: Created aiohttp client session
2023-04-08 19:55:51,872: Completed test setup
2023-04-08 19:55:51,872: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 19:55:51,872: ERROR   t1 (root file) [1]
2023-04-08 19:55:51,874: ERROR   t2 (root file) [2]
2023-04-08 19:55:51,875: ERROR   t3 (root file) [3]
2023-04-08 19:55:51,875: ERROR   t4 (root file) [4]
2023-04-08 19:55:51,875: ERROR   t5 (root file) [5]
2023-04-08 19:55:51,875: ERROR   t6 (root file) [6]
2023-04-08 19:55:51,876: ERROR   t7 (root file) [7]
2023-04-08 19:55:51,877: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             FAIL
                        Tests:              7
                        Start:              2023-04-08 19-55-51
                        End:                2023-04-08 19-55-51
                        Duration:           0.003555115 seconds
                        Tags:               []
                        
                        PASS:               0
                        FAIL:               0
                        ERROR:              7
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                7
                        LOGGER:             0
                        UNEXPECTED:         0
```

<h4 id="10-logger-errors">10. Logger errors</h4>

- - -

- Developers can make __errors__ while coding
- __General__ error exception __messages__ will increase the time to __find__ and __fix__ these issues
- test_rest_api provides __short__ & __precise__ error's with exact __traceback__ info
- Here we are __purposefully__ making errors in __Logger__ functions

[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/logger_errors.html)

Console output

```bash
2023-04-08 21:54:56,023: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 21:54:56,023: Starting test setup
2023-04-08 21:54:56,023: Auto detecting test suites
2023-04-08 21:54:56,023: Total test suites: 1
2023-04-08 21:54:56,023: Auto detecting tests
2023-04-08 21:54:56,023: Total synchronous tests: 0
2023-04-08 21:54:56,023: Total asynchronous tests: 7
2023-04-08 21:54:56,023: Total tests: 7
2023-04-08 21:54:56,023: Created aiohttp client session
2023-04-08 21:54:56,023: Completed test setup
2023-04-08 21:54:56,023: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 21:54:56,023: ERROR   t1 (root file) [1]
2023-04-08 21:54:56,025: ERROR   t2 (root file) [2]
2023-04-08 21:54:56,025: ERROR   t3 (root file) [3]
2023-04-08 21:54:56,026: ERROR   t4 (root file) [4]
2023-04-08 21:54:56,026: ERROR   t5 (root file) [5]
2023-04-08 21:54:56,026: ERROR   t6 (root file) [6]
2023-04-08 21:54:56,026: ERROR   t7 (root file) [7]
2023-04-08 21:54:56,027: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             FAIL
                        Tests:              7
                        Start:              2023-04-08 21-54-56
                        End:                2023-04-08 21-54-56
                        Duration:           0.003578533 seconds
                        Tags:               []
                        
                        PASS:               0
                        FAIL:               0
                        ERROR:              7
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             7
                        UNEXPECTED:         0
```

<h4 id="11-unexpected-errors">11. Unexpected errors</h4>

- - -


[Click here to view the html report](https://raw.githack.com/troymjose/test_rest_api/main/assets/reports/unexpected_errors.html)

- Developers can make __errors__ while coding
- __General__ error exception __messages__ will increase the time to __find__ and __fix__ these issues
- test_rest_api provides __short__ & __precise__ error's with exact __traceback__ info
- Here we are __purposefully__ making unexpected errors in tests

Console output

```bash
2023-04-08 21:58:04,529: 
                          =======================================================
                        || ..................................................... ||
                        || ..................................................... ||
                        || ...........  T E S T - R E S T - A P I   ............ ||
                        || ..................................................... ||
                        || ..................................................... ||
                          =======================================================
                        
2023-04-08 21:58:04,529: Starting test setup
2023-04-08 21:58:04,530: Auto detecting test suites
2023-04-08 21:58:04,530: Total test suites: 1
2023-04-08 21:58:04,530: Auto detecting tests
2023-04-08 21:58:04,530: Total synchronous tests: 0
2023-04-08 21:58:04,530: Total asynchronous tests: 6
2023-04-08 21:58:04,530: Total tests: 6
2023-04-08 21:58:04,531: Created aiohttp client session
2023-04-08 21:58:04,531: Completed test setup
2023-04-08 21:58:04,531: 
                          =======================================================
                        || ............... A S Y N C - T E S T S ............... ||
                          =======================================================
2023-04-08 21:58:04,531: ERROR   t1 (root file) [1]
2023-04-08 21:58:04,532: ERROR   t2 (root file) [2]
2023-04-08 21:58:04,533: ERROR   t3 (root file) [3]
2023-04-08 21:58:04,534: ERROR   t4 (root file) [4]
2023-04-08 21:58:04,534: ERROR   t5 (root file) [5]
2023-04-08 21:58:04,534: ERROR   t6 (root file) [6]
2023-04-08 21:58:04,535: 
                          =======================================================
                        || ..................................................... ||
                        || ............  T E S T - S U M M A R Y   ............. ||
                        || ..................................................... ||
                          =======================================================
                        
                        Status:             FAIL
                        Tests:              6
                        Start:              2023-04-08 21-58-04
                        End:                2023-04-08 21-58-04
                        Duration:           0.003570664 seconds
                        Tags:               []
                        
                        PASS:               0
                        FAIL:               0
                        ERROR:              6
                        DISABLE:            0
                        SKIP:               0
                        
                        LOW:                0
                        MINOR:              0
                        MAJOR:              0
                        CRITICAL:           0
                        BLOCKER:            0
                        
                        REST API:           0
                        GLOBAL VARIABLES:   0
                        BUG:                0
                        LOGGER:             0
                        UNEXPECTED:         6
```

<h2 id="author">Author</h2>

- [Troy M Jose](https://www.linkedin.com/in/troymjose/)

<h2 id="license">License</h2>

Copyright Troy M Jose, 2023.

Distributed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license, test_rest_api is free and
open source software.