#!/usr/bin/python3
"""Defines text file-reading function."""


def read_file(filename=""):
    """Print text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
