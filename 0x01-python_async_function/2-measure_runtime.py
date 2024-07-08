#!/usr/bin/env python3
"""
Module 2-measure_runtime
Contains the function measure_time.
"""

import time
import asyncio
from typing import List
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns the average time per coroutine.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        float: The average time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    
    total_time = end_time - start_time
    return total_time / n
