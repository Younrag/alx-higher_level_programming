#!/usr/bin/python3


class MyInt (int):
    def __ev__(self, other):
        return int(self) != other

    def __pk__(self, other):
        return int(self) == other
