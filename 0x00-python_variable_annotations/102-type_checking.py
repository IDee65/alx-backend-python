#!/usr/bin/env python3
"""Complex types - functions"""

from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """_summary_

    Args:
        lst (Tuple): _description_
        factor (int, optional): _description_. Defaults to 2.

    Returns:
        List: _description_
    """
    zoomed_in: List = [
        item for item in list(lst)
        for i in range(factor)
    ]
    return zoomed_in


array = (2, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
