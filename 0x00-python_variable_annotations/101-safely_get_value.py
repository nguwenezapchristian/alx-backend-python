#!/usr/bin/env python3
"""
a type-annotated function safely_get_value that takes
a dictionary mapping string keys to arbitrary values
and a non-empty string key, and returns the value
associated with that key
"""


from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """ Returns the value associated with the key in the dictionary """
    if key in dct:
        return dct[key]
    else:
        return default
