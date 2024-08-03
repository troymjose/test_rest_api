import logging
from typing import override


class TestRestApiReportFormatter(logging.Formatter):
    """ Custom formatter class to format test rest api report log records """

    def __init__(self, datefmt: str = "%Y-%m-%d %H:%M:%S %z"):
        """ Initialize custom formatter class with custom date time format """
        # Call parent class constructor
        super().__init__()
        # Set date time format
        self.datefmt = datefmt

    @override
    def format(self, record: logging.LogRecord) -> str:
        """ Override format method of logging.Formatter class to return custom string of log record message """
        # Get current date time with formatting
        datetime = self.formatTime(record=record, datefmt=self.datefmt)
        # Get log record message
        message = record.getMessage()
        # Create custom log record message by adding below details to log record message
        # 1. log level
        # 2. date & time
        # 3. dashed line
        custom_message = f"""
🗒️ <small>{record.levelname}</small>
⏱️ <i><small><small>{datetime}</small></small></i>

{message.strip()}
<hr style="border-top:dashed"></hr>"""
        # Return formatted log record message
        return custom_message
