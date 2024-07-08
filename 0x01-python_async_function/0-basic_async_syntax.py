#!/usr/bin/env python3
"""
Module 0-basic_async_syntax
Contains the function wait_random.
"""

import asyncio
import random
from typing import Union

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between 0 and max_delay
    (inclusive) seconds and eventually returns it.

    Args:
        max_delay (int): The maximum delay in seconds. Defaults to 10.

    Returns:
        float: The random delay time.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
