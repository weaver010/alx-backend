#!/usr/bin/env python3
'''Task 3: LRU Caching
'''

from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    '''A class `LRUCache` that inherits from
       `BaseCaching` and implements a caching system.
    '''

    def __init__(self):
        '''Sets up the cache
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Inserts an item into the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key, _ = self.cache_data.popitem(last=False)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Fetches an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
