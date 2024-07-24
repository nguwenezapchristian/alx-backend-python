#!/usr/bin/env python3
"""
A type-annotated function zoom_array that takes a tuple lst
and an integer factor as arguments and returns a tuple
"""

from typing import List, Tuple


def zoom_array(
        lst: Tuple[int, ...],
        factor: int = 2) -> Tuple[int, ...]:
    """Zoom array by repeating each item factor times"""
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return tuple(zoomed_in)
