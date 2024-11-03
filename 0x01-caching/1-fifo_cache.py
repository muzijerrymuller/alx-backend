#!/usr/bin/env python3
"""
FIFO caching
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    provides a structure for adding and accessing items
    in a dictionary-like cahe, where the oldest entries
    are removed first once the cache reaches its max capacity
    """
    def __init__(self):
        """
        This sets up the cache storage with the neccessary cofigurations
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        inserts item into cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """
        fetches an item from the cahce using its key
        """
        return self.cache_data.get(key, None)
