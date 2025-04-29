#!/usr/bin/env python3

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Retourne un dictionnaire avec les informations de pagination"""
        data = self.get_page(page, page_size)
        
        total_rows = len(self.dataset())
        total_pages = math.ceil(total_rows / page_size)
        
        # Déterminer la page suivante et la page précédente
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        
        # Retourner le dictionnaire
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
