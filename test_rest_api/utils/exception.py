class TestRestApiException(Exception):
    """
    Base Exception class
    """

    def format(self, exc, error_msg):
        """
        Format of reporting
        """
        _no_data_to_display = 'No data to display'
        return f"""
EXCEPTION
---------
{exc.strip() if exc.strip() else _no_data_to_display}

ERROR MESSAGE
-------------
{error_msg.strip() if error_msg.strip() else _no_data_to_display}
"""
