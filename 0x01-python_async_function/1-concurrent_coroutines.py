#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
Contains the function wait_n.
"""

import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: The list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        sorted_delays.append(min_delay)
        delays.remove(min_delay)
    
    return sorted_delays
