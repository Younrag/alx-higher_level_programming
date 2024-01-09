#!/usr/bin/python3
"""Modul"""


import json


def load_from_json_file(filename):
    """json"""
    with open(filename, "r", encoding="UTF-8") as f:
        return json.load(f)
