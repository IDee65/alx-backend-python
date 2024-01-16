#!/usr/bin/env python3
"""async_generator module """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator function """
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        yield random.random() * 10
        i += 1
