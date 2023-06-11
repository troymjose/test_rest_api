from inspect import getframeinfo, stack
from .. import settings
from ..testing.bug import Bug
from .exception import AssertException
from ..utils.decorator_hints import decorated_func_param_hints


@decorated_func_param_hints
def catch_exc(func):
    """
    Catch the exceptions and raise new exception
    AssertionError exception will be re raised using the bug obj passed
    Rest all errors will be raised as AssertException to make the test status as ERROR
    NOTE: We are a custom catch_exc, because we need raise assert with bug params which will be dynamic value
    """

    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except AssertionError as exc:
            assert False, exc.args[0]
        except Exception as exc:
            raise AssertException(msg=str(exc))

    return inner


class Assert:
    """
    Custom Assert Class for performing assertions
    Advantages of using this over python inbuilt assert statement -> Rich reporting for both pass and fail scenarios
    """

    @classmethod
    @catch_exc
    def equal(cls, arg1, arg2, bug=Bug()):
        """
        Check if arg1 == arg2
        Raise your custom Bug if needed
        """
        # Get the caller object to retrieve the caller code
        caller = getframeinfo(stack()[2][0])
        # Logging
        print(f"""
Assertion
---------
 {settings.logging.sub_point} Code   {settings.logging.key_val_sep} {caller.code_context[0].strip()}
 {settings.logging.sub_point} Assert {settings.logging.key_val_sep} assert {arg1} == {arg2}
""")
        # Perform the assertion using python inbuilt assert statement
        assert arg1 == arg2, bug
