#!/usr/bin/env python3

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task_wait_n

    Args:
        n (int): number of times
        max_delay (int): max delay

    Returns:
        List[float]: list of delays
    """
    tasks: List[float] = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
