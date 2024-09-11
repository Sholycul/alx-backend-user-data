#!/usr/bin/env python3
"""
Password encryption module
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt and returns the salted, hashed password.

    Args:
        password (str): The plain text password to be hashed.

    Returns:
        bytes: The salted, hashed password as a byte string.
    """
    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password using bcrypt with the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
