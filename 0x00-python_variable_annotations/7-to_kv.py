#!/usr/bin/env python3
"""Complex types - string and int/float to tuple"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple.

    Args:
        k (str): string
        v (Union[int, float]): int or float

    Returns:
        Tuple[str, float]: tuple
    """
    return (k, v ** 2)
