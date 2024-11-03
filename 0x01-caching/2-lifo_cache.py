#!/usr/bin/env python3
"""LIFO Cache Module: Where the Newest Comes First... to Go!
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """A cache system with a dramatic twist! The most recent
    item is the first to leave when space runs out.
    
    Items are stored in a dictionary, and when the cache
    reaches its max size, the last one in is the first one out.
    """
    def __init__(self):
        """Prepares an orderly cache for storing items with 
        a Last-In, First-Out approach.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds a new item to the cache with a LIFO flourish!
        
        If adding this item exceeds the cache limit, the most
        recent entry is dramatically removed to make space.
        
        Args:
            key: The identifier for the cached item.
            item: The data or object to be cached.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """Retrieves an item by its key, if it exists.
        
        Args:
            key: The key tied to the item you want to retrieve.
        
        Returns:
            The cached item if it exists; otherwise, None.
        """
        return self.cache_data.get(key, None)
