#!/usr/bin/env python3
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Calcule la somme des éléments d'une liste de nombres flottants.

    Args:
        input_list (List[float]): Une liste de nombres flottants.

    Returns:
        float: La somme des nombres dans la liste.
    '''
    return sum(input_list)
