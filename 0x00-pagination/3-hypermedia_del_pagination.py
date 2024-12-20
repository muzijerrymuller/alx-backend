#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        this part of the code allows for
        the pagination to be deletion-resiliant
        by allowing acess by index even if items are removed
        """

        dataset = self.indexed_dataset()
        data_length = len(dataset)
        if index is None or index < 0 or index >= data_length:
            raise IndexError("Index out of range")

        page_data = []
        next_index = index
        while len(page_data) < page_size and next_index < data_length:
            item = dataset.get(next_index)
            if item:
                page_data.append(item)
            next_index += 1

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(page_data),
            "data": page_data
        }
