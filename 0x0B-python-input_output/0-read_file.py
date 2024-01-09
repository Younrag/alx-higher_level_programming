#!/usr/bin/python3
"""Modul"""


def read_file(filename=""):
    """read file"""
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
