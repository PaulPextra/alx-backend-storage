#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""

import redis
import sys
from typing import Union, Optional, Callable
from uuid import uuid4


class Cache:
    """
    Cache class.
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generates a random key using uuid, store the input data and return the key.
        """

        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """ Get Method  """

        result = self._redis.get(key)
        return fn(result) if fn else result

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string """

        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integer """

        return int.from_bytes(data, sys.byteorder)
