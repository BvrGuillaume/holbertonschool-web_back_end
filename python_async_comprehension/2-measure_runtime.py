#!/usr/bin/env python3
"""Measure_runtime coroutine that will execute."""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension

# La fonction measure_runtime mesure le temps total d'exécution
async def measure_runtime() -> float:
    """heure de début"""
    start = time.time()

    """Exécution parallèle des 4 appels à async_comprehension"""
    """asyncio.gather permet d'exécuter les tâches simultanément"""
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    """enregistre l'heure de fin après que toutes les tâches soient terminé"""
    end = time.time()

    """renvoie la différence entre l'heure de fin et l'heure de début"""
    return end - start
