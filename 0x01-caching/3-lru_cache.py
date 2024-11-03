#!/usr/bin/env python3
"""
Cache Module with Flair: Least Recently Used (LRU) Caching System.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    A caching system that evicts the least recently accessed
    items with finesse, ensuring only the freshest data remains.
    This cache manages items with an LRU (Least Recently Used) policy,
    seamlessly removing the oldest unused item when the limit is reached.
    """
    def __init__(self):
        """
        Prepares the cache, primed and ready to store data with style!
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Adds an item to the cache, preserving only the most active entries.
        If the cache reaches its max capacity,
        the least recently accessed item
        is gracefully shown the door, freeing space for fresh data!
        Args:
            key: The unique identifier for the item to store.
            item: The data or object to be cached.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetches an item from the cache and refreshes its place in line.
        This action marks the item as recently used, showcasing its value
        by keeping it near the front of the cache.
        Args:
            key: The identifier of the item to retrieve.
        Returns:
            The cached item if available; otherwise, None.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
