import sys
from test_rest_api.testing.runner import runner
from test_rest_api.utils.error_msg import ErrorMsg

if __name__ == "__main__":
    # Validate if the user provided minimum number of required params in the command
    if len(sys.argv) < 3:
        sys.exit(ErrorMsg.INVALID_COMMAND)
    # Get the arguments
    command, test_suite_path = sys.argv[1], sys.argv[2]
    # Run command
    if command == '-t':
        # Run the test suite
        runner.run(path=test_suite_path)
    else:
        sys.exit(ErrorMsg.INVALID_COMMAND)
