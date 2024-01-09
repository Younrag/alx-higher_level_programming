#!/usr/bin/python3
"""Modul"""


def append_write(filename="", text=""):
    """write append"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
