#!/usr/bin/python

"""
An example Python file to demonstrate and test the pydocmd Markdown generator.
"""

import sys
import os


__author__ = "Ferry Boender"
__copyright__ = "Copyright 2014, Ferry Boender"
__license__ = "MIT (expat) License"
__version__ = "0.1"
__maintainer__ = "Ferry Boender"
__email__ = "ferry.boender@gmail.com"


CONST_BLUE="#0000FF"
CONST_RED="#FF0000"

def hello(name="World"):
    """
    Print "Hello, <name>" to stdout
    """
    print "Hello, %s!" % (name)


class Arithmetic:
    """
    Arithmetic is an arithmetic class that can perform summing or subtraction
    on two numbers.
    """
    def __init__(self, x, y):
        """
        Construct a new Arithmetic instance. `x` and `y` are the numbers this
        class will be performing arithmetic on.
        """
        self.x = x
        self.y = y

    def sum(self, x=None, y=None):
        """
        Returns the sum of `x` and `y`. If `x` or `y` is None, it will use the
        values set at instantiation.
        """
        if x is None:
            x = self.x
        if y is None:
            y = self.y

        return x + y

    def sub(self, x=None, y=None):
        """
        Returns `y` subtracted from `x`. If `x` or `y` is None, it will use the
        values set at instantiation.
        """
        if x is None:
            x = self.x
        if y is None:
            y = self.y

        return x - y


if __name__ == "__main__":
    hello()
    a = Arithmetic(10, 5)
    print a.sum()
    print a.sum(x=5)
    print a.sub()
    print a.sub(y=15)
