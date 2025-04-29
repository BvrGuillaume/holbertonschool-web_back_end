#!/usr/bin/env python3
"""Module containing a simple function to calculate pagination indexes"""
def index_range(page, page_size):
    """
    Returns a tuple containing the start and end indexes for pagination.
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)
