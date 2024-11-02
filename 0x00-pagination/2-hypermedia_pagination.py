#!/usr/bin/env python3
"""
Fundamental Pagination Sample.
"""
import math
import csv
from typing import List, Tuple
from typing import Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Derives the range of indices based on the given page
    number and size specifications.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """
    Server Class for Managing and Paginating Baby Names Database Records.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Configures a new server instance.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        saved data set for an improvement of performance.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        saves data from corresponding data set.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Retrieves information about a specified page,
        including key metadata like title, description,
        author, and publication date, for use in analysis or reporting.
        """
        data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages
        }
