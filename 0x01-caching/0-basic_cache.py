#!/usr/bin/env python3

'''Task 0: Basic dictionary
'''

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    '''A class `BasicCache` that inherits from `BaseCaching`
       and serves as a caching system
    '''

    def put(self, key, item):
        '''Store the `item` in the dictionary `self.cache_data` with
           `key` as the identifier
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Retrieve the value from `self.cache_data` associated with `key`
        '''
        return self.cache_data.get(key, None)

