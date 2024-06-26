#!/usr/bin/env python3

'''Task 1: FIFO caching
'''

from collections import OrderedDict
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` and implements a caching system.
    '''

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Store the `item` in the dictionary `self.cache_data` with
           `key` as the identifier
        '''

        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

        self.cache_data[key] = item

    def get(self, key):
        '''Retrieve the value from `self.cache_data` associated with `key`
        '''
        return self.cache_data.get(key, None)
