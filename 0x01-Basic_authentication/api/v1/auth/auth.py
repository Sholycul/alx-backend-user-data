#!/usr/bin/env python3

from flask import request
from typing import List, TypeVar

class Auth:
    """Template for all authentication systems."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """For now, return False, logic will be added later."""
        return False

    def authorization_header(self, request=None) -> str:
        """For now, return None, will implement logic later."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """For now, return None, will implement logic later."""
        return None

