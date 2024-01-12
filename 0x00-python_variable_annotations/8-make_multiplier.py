#!/usr/bin/env python3
"""Complex types - functions"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): multiplier

    Returns:
        Callable[[float], float]: function that multiplies a float
        by multiplier
    """
    def multiply(n: float) -> float:
        """Returns the product of multiplier and n.

        Args:
            n (float): float

        Returns:
            float: product of multiplier and n
        """
        return n * multiplier
    return multiply
