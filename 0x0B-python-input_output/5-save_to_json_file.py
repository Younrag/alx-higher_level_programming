#!/usr/bin/python3
"""Modul"""


import json


def save_to_json_file(my_obj, filename):
    """json"""
    with open(filename, "w", encoding="UTF-8") as f:
        json.dump(my_obj, f)
