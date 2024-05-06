#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument (max_delay,
with a default value of 10) named wait_random that waits for a random
delay between 0 and max_delay (included and float value)
seconds and eventually returns it.
"""
import asyncio
import random
from typing import Union


async def wait_random(max_delay=10) -> Union[int | float]:
    """ an async function which returns a random float number """
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)