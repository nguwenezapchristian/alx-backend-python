#!/usr/bin/env python3
"""
an async routine called wait_n that takes in 2 int arguments
(in this order): n and max_delay. That spawn wait_random n times
with the specified max_delay
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to call wait_random.
        max_delay (int): The maximum delay for each call to wait_random.

    Returns:
        List[float]: A list of all the delays (float values) in ascending
        order.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
