#!/usr/bin/env python3
"""
0. Writing strings to Redis
"""

import redis
from typing import Union
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
