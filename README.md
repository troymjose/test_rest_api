<img alt="test_rest_api" src="https://raw.githubusercontent.com/troymjose/test_rest_api/main/test_rest_api.png"  width="50%" >

# TEST REST API

Create fast modern __asynchronous__ tests for __REST API__ testing

```#FAST #EASY #ASYNC #RESTAPI #TESTING #AUTOMATION```

- [Installation](#installation)
- [Examples](#examples)
    - [My first test](#1-my-first-test)
    - [Configure my test](#2-configure-my-test)
    - [My first logger](#3-my-first-logger)
    - [Set global variables value](#4-set-global-variables-value)
    - [Set global variables value as constant](#5-set-global-variables-value-as-constant)
    - [Get global variables value](#6-get-global-variables-value)
    - [My first bug](#7-my-first-bug)
    - [Configure my bug](#8-configure-my-bug)
- [Features](#features)
- [Author](#author)
- [License](#license)

<h2 id="installation">Installation</h2>
If you already have [Python](http://python.org/) with [pip](https://pip.pypa.io/) installed, you can simply run:

```pip install test_rest_api```

<h2 id="examples">Examples</h2>
- - -
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

``` python -m test_rest_api -t "test file path" -r "result folder path"```

- - -
<h4 id="2-configure-my-test">2. Configure my test</h4>
- - -

```python
from test_rest_api import test


@test(name='Custom Name', desc='Description', enabled=True, tags=['SMOKE', 'ALL'], is_async=True, execution_order='1')
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

- - -
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

- Loggers are used to add custom messages to the final html test report
- Create a new Logger __instance__ inside your test function```logger = Logger()```
- Logger instance __name__ can be any custom text. Here we have used __logger__
- Add any number of log messages using __log method__ ```logger.log("my 1st log")```
- Return logger instance for rich test __reporting__ ```return logger```
- It is __recommended__ to use logger for all your tests

- - -
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
- __is_constant__
    - Mandatory: False
    - Data Type: bool
    - Expected: True or False. Provide True, to create constants
    - Default: False

- - -
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
- To avoid this, we can set __constant__ values to global variables
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

- - -
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

- - -
<h4 id="7-my-first-bug">7. My first bug</h4>
- - -

```python
from test_rest_api import test, Bug


@test()
async def my_first_bug():
    Bug()
```

- Bug is used __raise issues__ in tests
- Add custom __checks__ in your tests to validate __rest api response__
- If __actual result__ is not the __expected result__, just call ```Bug()```
- This will __terminate__ the current test function execution
- Bug __details__ can be viewed in final html test __report__

- - -
<h4 id="8-configure-my-bug">2. Configure my bug</h4>
- - -

```python
from test_rest_api import test, Bug, Logger


@test()
async def my_second_bug():
    logger = Logger()
    logger.log('step 1')
    logger.log('step 2')
    logger.log('Consider all steps are logged')
    Bug(message="", priority=Bug.PRIORITY.BLOCKER, actual_result="", expected_result="", steps_to_reproduce=logger)
```

- In our first bug example, we used Bug() with __empty attributes__
- In this example, we are __using attributes__ to configure our Bug
- This can be considered as adding __more info__ to your bug in the final html test report
- We are adding custom __logging__ in this example to show how logger instance is __useful in Bug creation__
- Logger instance variable can be passed to __steps_to_reproduce__ attribute during Bug creation


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
    - Expected: Logger instance can be used to auto-populate this field ```logger```
    - Default: Empty string

[//]: # (Example 2: Test with parameters)

[//]: # ()

[//]: # (```python)

[//]: # (from test_rest_api import test, RestApi, Bug)

[//]: # ()

[//]: # ()

[//]: # (@test&#40;&#41;)

[//]: # (async def my_func_name&#40;&#41;:)

[//]: # (    # Create Product Rest Api Object)

[//]: # (    products = RestApi&#40;url="https://dummyjson.com/products/1"&#41;)

[//]: # (    # Send rest api &#40;method: GET&#41;)

[//]: # (    response = await products.get&#40;&#41;)

[//]: # (    # Check for 200 response status code)

[//]: # (    if response.status_code != 200:)

[//]: # (        # Raise Bug)

[//]: # (        Bug&#40;&#41;)

[//]: # (```)

## Test Execution

An example of a simple test execution command:

__Syntax__

``` python -m test_rest_api -t "<Path of test folder or file>" -r "<Path to save test report>" ```   
__Example__

``` python -m test_rest_api -t "/Users/user/Documents/TestSuite" -r "/Users/user/Documents/TestResult" ```

## Features

- __Asyncronus__ programming (Powered by [asyncio](https://pypi.org/project/asyncio/))
- One of the __fastest__ python rest api test frameworks available
- Supports both asyncronus & __syncronuous__ tests
- __Auto discovery__ of test modules and functions
- Beautifull rich __html test reporting__ with dashboards
- Detailed info on unexpected errors while creating automaton tests
- Fast to code, increase the speed to develop tests by about 200% to 300%
- Designed to be easy to use and learn
- Supports end-to-end testing with __CI/CD pipelines__
- Supports __parameterization__, __correlation__ and __logging__
- Supports selective test executions using hashtags eg: __#smoke__

## Author

- [Troy M Jose](https://www.linkedin.com/in/troymjose/)

## License

Copyright Troy M Jose, 2023.

Distributed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license, pytest is free and open    
source software.