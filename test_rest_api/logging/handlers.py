import logging
from typing import override
from ..reporting.report import report


class TestRestApiReportHandler(logging.Handler):
    """
    Custom handler class to add log record message to test rest api report
    This class inherits logging.Handler class and will help to add log record message directly to test rest api report
    """

    @override
    def emit(self, record):
        """ Override emit method of logging.Handler class to add log record message to test rest api report """
        # Get log record message after formatting
        message = self.format(record)
        # Get asyncio task name from log record
        asyncio_task = record.taskName
        # Add log record message to test rest api report
        report.add_message_to_logs(asyncio_task=asyncio_task, message=message)
        # Update the test report extras based on the log record
        if (item_to_be_updated := getattr(record, 'update_report_extras', None)) is not None:
            # Call the respective method to update the extras based on the log record
            # Example: update_extras_assertions, update_extras_requests, update_extras_responses etc
            getattr(report, f'update_extras_{item_to_be_updated}', None)(asyncio_task=asyncio_task)
