#!/usr/bin/env python3
""" measure runtime """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ measure time

    Args:
        n (int): number of times to call wait_random
        max_delay (int): max delay

    Returns:
        float: total time / n
    """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed: float = (time.perf_counter() - start) / n
    return elapsed
