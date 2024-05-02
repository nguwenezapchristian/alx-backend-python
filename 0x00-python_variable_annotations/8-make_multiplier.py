#!/usr/bin/env python3
"""
a type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Make_multiplier func returns a function """
    def fun(x: float) -> float:
        """ multiplies the multiplier and a float passed to returned func"""
        return x * multiplier
    
    return fun