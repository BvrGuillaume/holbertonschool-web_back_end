#!/usr/bin/env python3
""" this module contains a function to filter data from csv file """
import csv
import math
from typing import List


def index_range(page, page_size):
    """
    Retourne un tuple contenant les indices de début et de fin pour la pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retourne la page demandée du dataset"""
        # Vérification que page et page_size sont des entiers > 0
        assert isinstance(page, int) and page > 0,"page doit être un entier positif"
        assert isinstance(page_size, int) and page_size > 0,"page_size doit être un entier positif"
        
        """Obtenir les indices de la page à afficher"""
        start_index, end_index = index_range(page, page_size)
        
        """Récupérer le dataset"""
        dataset = self.dataset()

        """Vérifier si les indices sont valides et renvoyer la page correspondante"""
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
