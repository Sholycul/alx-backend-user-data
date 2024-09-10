#!/usr/bin/env python3
"""
Module for filtering log messages by obfuscating specific fields.
"""

import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates fields in a log message.
    
    Args:
        fields (List[str]): The list of fields to obfuscate.
        redaction (str): The string to replace the field values with.
        message (str): The log message.
        separator (str): The character separating the fields.

    Returns:
        str: The obfuscated log message.
    """
    for field in fields:
        pattern = f'{field}=.*?{separator}'
        replacement = f'{field}={redaction}{separator}'
        message = re.sub(pattern, replacement, message)
    return message

