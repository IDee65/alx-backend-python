#!/usr/bin/env python3
"""Complex types - list of floats"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements and their lengths.

    Args:
        lst (Iterable[Sequence]): list of floats

    Returns:
        List[Tuple[Sequence, int]]: list of tuples containing elements
        and their lengths
    """
    return [(i, len(i)) for i in lst]
