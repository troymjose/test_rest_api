from .runner import runner


def skip_test(*, tags: str) -> bool:
    """
    Checks if we need to Skip the test or not
    returns True for skipping the test
    returns False for not skipping the test
    """
    # Check if we have any tags for test execution
    if not runner.test_tags:
        return False
    # Format current test tags by removing '#' from the starting of the string
    tags = [tag[1:] if tag.startswith("#") else tag for tag in tags]
    # Check for #ALL (This will run for all tag cases, eg: login api)
    if 'ALL' in tags:
        return False
    # Check if any of the runner test tag is present in the current test else skip the test
    if any(test_tag in tags for test_tag in runner.test_tags):
        return False
    # Skip the test
    return True
