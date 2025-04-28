#!/usr/bin/env python3
"""Coroutine called async_generator that takes no args"""
import asyncio
import random

async def async_generator():
    """The coroutune will loop 10 times"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
