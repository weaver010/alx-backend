#!/usr/bin/python3
"""LFU Cache Replacement Implementation Class
"""
from threading import RLock

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Implements an LFUCache (Least Frequently Used).

    Attributes:
        __stats (dict): A dictionary tracking the access count for each cache key.
        __rlock (RLock): Lock to synchronize access and prevent race conditions.
    """
    def __init__(self):
        """Initializes the cache and sets instance attributes.
        """
        super().__init__()
        self.__stats = {}
        self.__rlock = RLock()

    def put(self, key, item):
        """Inserts an item into the cache.
        """
        if key is not None and item is not None:
            keyOut = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if keyOut is not None:
                print('DISCARD: {}'.format(keyOut))

    def get(self, key):
        """Fetches an item by key.
        """
        with self.__rlock:
            value = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return value

    def _balance(self, keyIn):
        """Removes the least frequently used item if the cache size limit is reached.
        """
        keyOut = None
        with self.__rlock:
            if keyIn not in self.__stats:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    keyOut = min(self.__stats, key=self.__stats.get)
                    self.cache_data.pop(keyOut)
                    self.__stats.pop(keyOut)
            self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return keyOut
