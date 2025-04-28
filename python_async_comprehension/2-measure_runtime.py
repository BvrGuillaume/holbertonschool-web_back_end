#!/usr/bin/env python3
"""Measure_runtime coroutine that will execute."""

import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    start_time = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time.perf_counter()
    return end_time - start_time
'''Mesure le temps d'exécution total de 4 exécutions de async_comprehension en parallèle et retourne le temps d'éxécution '''
