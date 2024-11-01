#!/usr/bin/env python3
"""Simple pagination example for managing and retrieving paginated
data from a dataset of popular baby names. The script demonstrates 
basic pagination techniques by defining an index range function to 
determine data slicing boundaries and a server class to cache, 
retrieve, and paginate data.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculates the starting and ending 
    index for a given page and page size.

    This function is used to determine the range of rows that should
    be returned based on the current page and the number of records
    per page (`page_size`). It calculates the start index as the 
    product of `(page - 1) * page_size` and the end index as 
    `start + page_size`, effectively covering all items on the 
    specified page.

    Args:
        page (int): The page number (starting from 1).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple of two integers representing the start
                         and end indexes for slicing the dataset.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to handle and paginate a dataset of popular baby names.

    The `Server` class loads a CSV file of popular baby names and caches
    it in memory, allowing for efficient repeated access. The class 
    provides a method `get_page` to return paginated slices of the data 
    based on a given page and page size, leveraging the `index_range`
    helper function to determine the appropriate slice.
    Attributes:
        DATA_FILE (str): The path to the CSV file containing the dataset.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes a new Server instance and prepares the dataset cache.

        The `__dataset` attribute is initially set to `None`, indicating
        that the dataset has not been loaded yet. This lazy-loading approach
        means the dataset will only be loaded into memory the first time
        it is needed, avoiding unnecessary file reads and memory usage 
        if the data is never requested.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Loads the dataset from a CSV file
        into memory if not already loaded.

        This method reads from the CSV file specified by `DATA_FILE` and
        loads the contents into a list of lists, excluding the header row.
        The loaded data is cached in the `__dataset` attribute to improve
        performance for subsequent accesses by avoiding repeated file I/O.
        If the dataset is already cached, the method simply returns the
        cached data, minimizing file access.
        Returns:
            List[List]: A list of lists representing rows from the CSV file,
            where each inner list corresponds to a row in the dataset.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a specific page of data from the dataset.

        Uses the `page` and `page_size` arguments to calculate the
        appropriate start and end indices for pagination. The method
        first verifies that both arguments are positive integers using 
        assertions to prevent invalid values. It then uses the
        `index_range` function to determine the slice boundaries for
        the dataset and returns the corresponding rows as a paginated
        view. If the starting index exceeds the dataset's length, it
        returns an empty list.
        Args:
            page (int): The page number (must be a positive integer).
            page_size (int): The number of items per page (must be positive).
        Returns:
            List[List]: A list of lists representing rows
            for the specified page.
                        Returns an empty list if the
                        page number is out of range.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
