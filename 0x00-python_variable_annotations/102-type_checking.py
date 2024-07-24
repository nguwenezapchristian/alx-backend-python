#!/usr/bin/env python3
"""
a type-annotated function zoom_array that takes a list lst
and an integer factor as arguments and returns a list
"""

from typing import List, Tuple


def zoom_array(lst: List, factor: int = 2) -> List:
    """ Zoom array """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
