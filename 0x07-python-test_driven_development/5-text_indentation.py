#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    h = 0
    while h < len(text) and text[h] == ' ':
        h += 1

    while h < len(text):
        print(text[h], end="")
        if text[h] == "\n" or text[c] in ".?:":
            if text[h] in ".?:":
                print("\n")
            c += 1
            while h < len(text) and text[h] == ' ':
                h += 1
            continue
        h += 1
