#!/usr/bin/env python3
"""
Module 3-tasks
Contains the function task_wait_random.
"""

import asyncio
from 0-basic_async_syntax import wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay in seconds.

    Returns:
        asyncio.Task: The created asyncio.Task for wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
