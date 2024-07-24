#!/usr/bin/env python3
"""
a type-annotated function safe_first_element that takes
a list lst and returns the first element of the list
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first element of the list """
    if lst:
        return lst[0]
    else:
        return None
