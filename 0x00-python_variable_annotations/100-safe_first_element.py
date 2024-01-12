#!/usr/bin/env python3
"""Complex types - mixed list"""

from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of a list.

    Args:
        lst (Sequence[Any]): list of any type

    Returns:
        Union[Any, None]: first element of a list
    """
    if lst:
        return lst[0]
    else:
        return None
