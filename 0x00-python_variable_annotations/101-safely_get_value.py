#!/usr/bin/env python3
"""More involved type annotations"""

from typing import Any, Union, Mapping, TypeVar

T = TypeVar('T')
NoneType = TypeVar('NoneType', None, None)
R = Union[Any, T]
D = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: D) -> R:
    """Returns the value safely.

    Args:
        dct (Mapping): mapping
        key (Any): key
        default (Default, optional): default value. Defaults to None.

    Returns:
        Return: value
    """
    if key in dct:
        return dct[key]
    else:
        return default
