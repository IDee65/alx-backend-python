#!/usr/bin/env python3
"""Complex types - mixed list"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns their sum as a float.

    Args:
        mxd_lst (List[Union[int, float]]): list of floats

    Returns:
        float: sum of the list as a float
    """
    return sum(mxd_lst)
