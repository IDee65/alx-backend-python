#!/usr/bin/env python3
""" Let's execute multiple coroutines at the same time with async """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """ wait_n coroutine

    Args:
        n (int, optional): number of times to call wait_random. Defaults to 0.
        max_delay (int, optional): max delay Defaults to 10.

    Returns:
        List[float]: list of all the delays
    """
    delays: List[float] = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))
    return sorted(delays)
