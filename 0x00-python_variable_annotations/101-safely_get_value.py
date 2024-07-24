#!/usr/bin/env python3
"""
A type-annotated function safely_get_value that takes
a dictionary mapping keys to arbitrary values
and a key, and returns the value associated with that key,
or a default value if the key is not present.
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value associated with the key in the dictionary,
    or default if the key is not present.
    """
    if key in dct:
        return dct[key]
    else:
        return default
