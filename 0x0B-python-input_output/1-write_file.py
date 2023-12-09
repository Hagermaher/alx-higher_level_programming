#!/usr/bin/python3
"""Define writing file function."""


def write_file(filename="", text=""):
    """Write string to file.

    Args:
        filename (str): filename
        text (str): text
    Returns: number
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
