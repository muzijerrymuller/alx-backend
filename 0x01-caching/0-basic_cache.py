#!/usr/bin/env python3

'''Task 0: Basic dictionary caching system.
This module implements a basic caching system in the form of the `BasicCache` class. 
The `BasicCache` class provides a fundamental framework for storing and retrieving key-value 
pairs without any cache eviction policies. This is suitable for scenarios where unlimited 
cache size is acceptable, and keys and values are not expected to expire or be evicted 
automatically.

By inheriting from `BaseCaching`, this class is designed to support a dictionary-based 
cache system that stores values associated with specific keys. `BasicCache` provides two 
core functionalities: adding items to the cache using the `put` method and retrieving 
items from the cache using the `get` method. This implementation demonstrates how to 
implement a caching system without restrictions on size, as the cache will continue 
to grow with every added item until it potentially reaches memory limits.
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching` and serves as 
       a basic caching system that stores key-value pairs in a dictionary 
       (`self.cache_data`). It does not include any eviction mechanism, 
       meaning that it will keep adding items until memory limitations 
       are reached. This class provides methods for adding new cache 
       entries and retrieving existing ones.
       
       Attributes:
           cache_data (dict): A dictionary inherited from `BaseCaching`, 
           used to store all cached items where each key maps to a specific 
           item value. This cache data structure will hold all entries added 
           via the `put` method, which allows items to be stored without 
           limitation on cache size.
    '''

    def put(self, key, item):
        '''Assigns the provided `item` value to the specified `key` within 
           the dictionary `self.cache_data`. This method will only add the 
           item if both `key` and `item` are not `None`. If either is `None`, 
           the method does nothing, ensuring that the cache only contains 
           valid key-value pairs. This method enables the caching system 
           to store data by associating it with a unique key, allowing 
           for fast and efficient retrieval.

           Args:
               key (str): The unique identifier used to store and retrieve 
               data within the cache. If `key` is not `None`, it will serve 
               as the dictionary key for accessing the associated item value.
               item (Any): The actual data or value associated with `key`. 
               When added to the cache, `item` will be accessible through the 
               corresponding `key` provided to this method.

           Returns:
               None: This method does not return a value. Instead, it updates 
               the `self.cache_data` dictionary with the new key-value pair, 
               expanding the cache as new entries are added without any 
               restrictions or limits.
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Retrieves the value in `self.cache_data` that is associated with 
           the specified `key`. If the `key` is present in the cache, the 
           method will return the corresponding value. If the `key` is not 
           found, the method returns `None`, indicating that the requested 
           data is not available in the cache.

           This method leverages the dictionary `.get()` function, which 
           allows for safe retrieval without raising an error if `key` does 
           not exist in the cache. As a result, this caching system enables 
           graceful handling of requests for non-existent keys, returning 
           `None` instead of causing program interruptions.

           Args:
               key (str): The unique identifier for the cached value that 
               the method is attempting to retrieve. If `key` is not found 
               in the cache, the method returns `None`.

           Returns:
               Any: The value associated with `key` in the cache, if it exists. 
               If `key` is not in `self.cache_data`, the method returns `None`, 
               indicating the absence of data for that key.
        '''

        return self.cache_data.get(key, None)
