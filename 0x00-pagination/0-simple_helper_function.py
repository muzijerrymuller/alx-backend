#!/usr/bin/env python3
"""
Pagination
"""


from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Pagination helper function that retrieves
    range from given page & page size
    """
    starting = (page - 1) * page_size
    ending = start + page_size
    return (starting, ending)
