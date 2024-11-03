#!/usr/bin/env python3
"""Dynamic Caching Module: Most Recently Used (MRU) Caching Strategy.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A sophisticated caching solution that efficiently manages
    data storage by utilizing the Most Recently Used (MRU) removal
    strategy. This cache dynamically retains the most relevant
    data while ensuring optimal performance and memory usage.

    When the cache limit is reached, the least recently used item is
    removed, promoting a streamlined caching experience.
    """
    def __init__(self):
        """Initializes the MRU cache, setting the stage for high-performance
        data management. This constructor prepares the cache by establishing
        an ordered dictionary to maintain the access order of cached items.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Inserts an item into the cache, ensuring that the most
        relevant data is stored for quick retrieval.

        If the cache exceeds its maximum capacity, the least recently
        used item is discarded, making room for new data while
        maintaining efficiency.

        Args:
            key: A unique identifier for the item being cached.
            item: The data or object to be stored in the cache.

        If either the key or item is None, this method does nothing,
        safeguarding against invalid entries.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item from the cache based on its key, ensuring
        that frequently accessed data remains easily accessible.

        When an item is accessed, it is marked as most recently used,
        thereby influencing the cache's eviction policy.

        Args:
            key: The unique identifier for the cached item.

        Returns:
            The cached item if it exists; otherwise, returns None.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
