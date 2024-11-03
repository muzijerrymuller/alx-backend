#!/usr/bin/env python3
"""Efficient Caching Module: Least Frequently Used (LFU) Strategy.
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """A powerful caching solution that implements
    the Least Frequently Used (LFU) strategy, optimizing memory
    usage and performance by removing the least accessed
    items when the cache limit is reach
    This cache is ideal for scenarios where
    certain items are accessed more often than
    others, ensuring that the most valuable
    data remains readily available.
    By tracking the frequency of access, this
    cache intelligently manages data,
    providing quick access to frequently used
    items while efficiently discarding
    those that are rarely needed.
    """
    def __init__(self):
        """Initializes the LFU cache, establishing the
        foundation for optimal data
        management. This constructor creates an ordered
        dictionary to store cached
        items and a list to keep track of the
        frequency of access for each item.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_freq = []

    def __reorder_items(self, mru_key):
        """Reorders the cache items based on the
        most recently used key, adjusting
        their frequency of access. This private
        method updates the frequency list
        to reflect the recent access, ensuring
        that the LFU strategy effectively
        identifies which item should be discarded
        when the cache limit is reached.
        Args:
            mru_key: The key of the item that was
            recently accessed, used to update
            its frequency and position in the access order.
        """
        max_positions = []
        mru_freq = 0
        mru_pos = 0
        ins_pos = 0
        
        for i, key_freq in enumerate(self.keys_freq):
            if key_freq[0] == mru_key:
                mru_freq = key_freq[1] + 1
                mru_pos = i
                break
            elif len(max_positions) == 0 or key_freq[1] < self.keys_freq[max_positions[-1]][1]:
                max_positions.append(i)

        max_positions.reverse()
        for pos in max_positions:
            if self.keys_freq[pos][1] > mru_freq:
                break
            ins_pos = pos

        self.keys_freq.pop(mru_pos)
        self.keys_freq.insert(ins_pos, [mru_key, mru_freq])

    def put(self, key, item):
        """Adds a new item to the cache or updates
        an existing item, maintaining
        the integrity of the LFU strategy.
        This method ensures that when the cache
        reaches its maximum capacity,
        the least frequently used item is discarded
        to make room for the new entry.
        Args:
            key: A unique identifier for the item to be cached.
            item: The data or object to be stored in the cache.
        If either the key or item is None,
        the operation is ignored to avoid
        invalid entries.
        """
        if key is None or item is None:
            return
        
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.keys_freq.pop()
                print("DISCARD:", lfu_key)
                
            self.cache_data[key] = item
            ins_index = len(self.keys_freq)
            
            for i, key_freq in enumerate(self.keys_freq):
                if key_freq[1] == 0:
                    ins_index = i
                    break
            self.keys_freq.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item from the cache based on
        its unique key, marking it as
        recently used to influence the LFU eviction
        policy. This method not only
        returns the requested item but also ensures
        that frequently accessed data
        remains accessible for subsequent operations.
        Args:
            key: The unique identifier for the cached item.
        Returns:
            The cached item if found; otherwise, returns None.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
