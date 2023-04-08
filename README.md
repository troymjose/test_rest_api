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

<h2 id="author">Author</h2>

- [Troy M Jose](https://www.linkedin.com/in/troymjose/)

<h2 id="license">License</h2>

Copyright Troy M Jose, 2023.

Distributed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license, test_rest_api is free and
open source software.