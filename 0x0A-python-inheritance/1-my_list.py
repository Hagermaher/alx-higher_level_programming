#!/usr/bin/python3
"""Defines an inherited list."""


class MyList(list):
    """Implements sorted printing."""

    def print_sorted(self):
        """Print sorted ascending order."""
        print(sorted(self))
