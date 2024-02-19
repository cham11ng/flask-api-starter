"""
Enum classes.
"""

from enum import Enum


class Codes(Enum):
    """Codes enum class."""

    NOT_FOUND = "FC404"
    INTERNAL_SERVER_ERROR = "FC500"
    METHOD_NOT_ALLOWED = "FC405"
