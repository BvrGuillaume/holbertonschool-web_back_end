#!/usr/bin/env python3
"""Coroutine called async_generator that takes no args"""
import asyncio
import random
import typing

async def async_generator()-> typing.AsyncGenerator[float, None]:
    """The coroutune will yield a random float between 0 and 10, 10 times"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
