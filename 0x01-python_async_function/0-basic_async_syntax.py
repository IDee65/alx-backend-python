#!/usr/bin/env python3
""" Wait random module """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait random coroutine

    Args:
        max_delay (int, optional): max delay Defaults to 10.

    Returns:
        float: slept time
    """
    sleep_time: float = random.random() * max_delay
    await asyncio.sleep(sleep_time)
    return sleep_time
