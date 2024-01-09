#!/usr/bin/python3
"""Modul"""


def write_file(filename="", text=""):
    """write file"""
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
