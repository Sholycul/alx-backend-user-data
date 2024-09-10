#!/usr/bin/env python3
"""
This module provides a logger with a formatter that redacts sensitive
personal identifiable information (PII) from log messages.
"""

import logging
import re
from typing import List


# Fields considered PII from user_data.csv
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Obfuscates the values of PII fields in a log message.

    Args:
        fields (List[str]): List of PII fields to redact.
        redaction (str): String to replace the PII values with.
        message (str): The log message containing PII.
        separator (str): The character separating fields in the log message.

    Returns:
        str: The log message with PII fields redacted.
    """
    for field in fields:
        message = re.sub(
            f'{field}=[^{separator}]*', f'{field}={redaction}', message
        )
    return message


class RedactingFormatter(logging.Formatter):
    """
    Formatter class that redacts PII from log messages.
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the formatter with the list of PII fields.

        Args:
            fields (List[str]): List of PII fields to redact.
        """
        super().__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Formats the log record, redacting PII fields.

        Args:
            record (logging.LogRecord): The log record.

        Returns:
            str: The formatted log record with PII redacted.
        """
        message = super().format(record)
        return filter_datum(self.fields, self.REDACTION, message, self.SEPARATOR)


def get_logger() -> logging.Logger:
    """
    Creates a logger named 'user_data' with INFO level and a StreamHandler
    that uses the RedactingFormatter.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    formatter = RedactingFormatter(fields=PII_FIELDS)
    stream_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)

    return logger

