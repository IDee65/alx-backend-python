#!/usr/bin/env python3
"""Complex types - list of floats"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns their sum as a float.

    Args:
        input_list (List[float]): list of floats

    Returns:
        float: sum of the list as a float
    """
    return sum(input_list)
